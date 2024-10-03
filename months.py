class Transaction:
    def __init__(self, transaction_type, company, amount, date):
        self.transaction_type = transaction_type
        self.company = company
        self.amount = amount
        self.date = date
    def __str__(self):
        return f"Transaction({self.transaction_type}, {self.company}, {self.amount}, {self.date})"

class CashbackCalculator:
    def __init__(self, transactions):
        self.transactions = transactions
        self.cashback_data = {}  # Structure: { month: { company: cashback_amount } }

    def process_transactions(self):
        for transaction in self.transactions:
            date_str = transaction.date
            month = date_str[5:7]  # Extract month as 'MM'

            # Getting cashback amount
            amount = transaction.amount
            if transaction.transaction_type == "REFUNDED":
                amount = -abs(amount)
            elif transaction.transaction_type == "PURCHASED":
                amount = abs(amount)
            else:
                continue

            if month not in self.cashback_data:
                self.cashback_data[month] = {}
            if transaction.company not in self.cashback_data[month]:
                self.cashback_data[month][transaction.company] = 0.0

            self.cashback_data[month][transaction.company] += amount

    def top_n_cashback_businesses(self, n, month):
        if month not in self.cashback_data:
            return []  # No data for the given month
        company_cashbacks = self.cashback_data[month]
        sorted_companies = sorted(company_cashbacks.items(), key=lambda item: item[1], reverse=True)
        return sorted_companies[:n]

# Sample transaction data
transactions_list = [
    Transaction("PURCHASED", "CompanyA", 100.0, "2023-01-15 10:00:00"),
    Transaction("PURCHASED", "CompanyB", 200.0, "2023-01-20 12:30:00"),
    Transaction("REFUNDED", "CompanyA", 50.0, "2023-01-25 15:45:00"),
    Transaction("PURCHASED", "CompanyC", 300.0, "2023-02-05 09:20:00"),
    Transaction("PURCHASED", "CompanyA", 250.0, "2023-02-10 11:15:00"),
    Transaction("REFUNDED", "CompanyB", 100.0, "2023-02-15 14:50:00"),
    Transaction("PURCHASED", "CompanyB", 150.0, "2024-01-05 08:30:00"),
    Transaction("PURCHASED", "CompanyC", 100.0, "2024-01-12 13:00:00")
]

# Initialize CashbackCalculator
calculator = CashbackCalculator(transactions_list)
calculator.process_transactions()

# Output the cashback data
print("Cashback Data:")
for month, companies in calculator.cashback_data.items():
    print(f"Month {month}:")
    for company, amount in companies.items():
        print(f"  {company}: ${amount:.2f}")

# Get top 2 companies for February
top_companies = calculator.top_n_cashback_businesses(2, '02')
print("\nTop 2 companies for February:")
for company, amount in top_companies:
    print(f"{company}: ${amount:.2f}")
