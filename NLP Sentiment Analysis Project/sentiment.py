import requests
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime, timedelta
import yfinance as yf

#Phase 1: get news data via newsapi.org

# Set your API key
api_key = '71015ea355524adaa5463cf1651763b6'

# Define the date range
end_date = datetime.now()
start_date = end_date - timedelta(days=30) # free tier caps us off at 30 days, so maybe we can do a day by day analysis?

# Fetch news articles
url = (f'https://newsapi.org/v2/everything?q=stock market&from={start_date.strftime("%Y-%m-%d")}'
       f'&to={end_date.strftime("%Y-%m-%d")}&language=en&sortBy=publishedAt&apiKey={api_key}')
response = requests.get(url)
# print(response.json())
articles = response.json()['articles']

#Store the articles in a pandas df (could use spark in future for improved performance/scalability)
df = pd.DataFrame(articles)
print(df[['publishedAt', 'title', 'description']])

#Phase 2: Pre-processing & Sentiment Analysis
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

# Function to get the sentiment score
def get_sentiment_score(text):
    return sid.polarity_scores(text)['compound'] if text else 0
df['sentiment'] = df['description'].apply(get_sentiment_score)
# df['sentiment'] = df['description'].apply(lambda x: sid.polarity_scores(x)['compound'] if x else 0)

#Converting publishedAt to datetime
df['publishedAt'] = pd.to_datetime(df['publishedAt'])

#Grouping by day and calculating average sentiment
df['day'] = df['publishedAt'].dt.date
daily_sentiment = df.groupby('day')['sentiment'].mean().reset_index()

#Grouping by week and calculating average sentiment
df['week'] = df['publishedAt'].dt.to_period('W').apply(lambda r: r.start_time)
weekly_sentiment = df.groupby('week')['sentiment'].mean().reset_index()

print(daily_sentiment)
print(weekly_sentiment)

#fetching stock market data for daily and weekly trends

# Define the stock ticker and date range
ticker = 'SPY'  # S&P 500 ETF as an example
end_date = datetime.now()
start_date = end_date - timedelta(days=30)
stock_data = yf.download(ticker, start=start_date, end=end_date, interval='1d')

# Calculate daily returns
stock_data['daily_return'] = stock_data['Adj Close'].pct_change()

# Reset the index to join with sentiment data
stock_data.reset_index(inplace=True)

# Convert Date to date
stock_data['Date'] = stock_data['Date'].dt.date

# Display the stock data
print("Stock Data with Daily Returns:\n", stock_data[['Date', 'daily_return']])

# Calculate weekly returns
stock_data['week'] = pd.to_datetime(stock_data['Date']).dt.to_period('W').apply(lambda r: r.start_time)
weekly_stock_data = stock_data.groupby('week').apply(lambda x: (x['Adj Close'].iloc[-1] - x['Adj Close'].iloc[0]) / x['Adj Close'].iloc[0]).reset_index()
weekly_stock_data.columns = ['week', 'weekly_return']

# Display the weekly stock data
print("Stock Data with Weekly Returns:\n", weekly_stock_data)

# Joining the sentiment dat with stock performance for daily and weekly trends and correlating them

# Merge daily sentiment and stock data
daily_combined_data = pd.merge(daily_sentiment, stock_data[['Date', 'daily_return']], left_on='day', right_on='Date', how='inner')

# Display the daily combined data
print("Daily Combined Data:\n", daily_combined_data[['day', 'sentiment', 'daily_return']])

# Calculate daily correlation
daily_correlation = daily_combined_data['sentiment'].corr(daily_combined_data['daily_return'])
print(f'Correlation between daily sentiment and daily stock performance: {daily_correlation}')
