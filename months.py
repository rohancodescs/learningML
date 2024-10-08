# transactions = [
#     ["PURCHASED", "CompanyA", 100.0, "2023-01-15 10:00:00"],
#     ["PURCHASED", "CompanyB", 200.0, "2023-01-20 12:30:00"],
#     ["REFUNDED", "CompanyA", 50.0, "2023-01-25 15:45:00"],
#     ["PURCHASED", "CompanyC", 300.0, "2023-02-05 09:20:00"],
#     ["PURCHASED", "CompanyA", 250.0, "2023-02-10 11:15:00"],
#     ["REFUNDED", "CompanyB", 100.0, "2023-02-15 14:50:00"],
#     ["PURCHASED", "CompanyB", 150.0, "2024-01-05 08:30:00"],
#     ["PURCHASED", "CompanyC", 100.0, "2024-01-12 13:00:00"]
# ]
class Transaction:
    def __init__(self, buyStatus, company, amount, date):
        self.buyStatus = buyStatus
        self.company = company
        self.amount = amount
        self.date = date
    def __str__(self):
        return f"Transaction({self.transaction_type}, {self.company}, {self.amount}, {self.date})"

transactions = [
    Transaction("PURCHASED", "CompanyA", 100.0, "2023-01-15 10:00:00"),
    Transaction("PURCHASED", "CompanyB", 200.0, "2023-01-20 12:30:00"),
    Transaction("REFUNDED", "CompanyA", 50.0, "2023-01-25 15:45:00"),
    Transaction("PURCHASED", "CompanyC", 300.0, "2023-02-05 09:20:00"),
    Transaction("PURCHASED", "CompanyA", 250.0, "2023-02-10 11:15:00"),
    Transaction("REFUNDED", "CompanyB", 100.0, "2023-02-15 14:50:00"),
    Transaction("PURCHASED", "CompanyB", 150.0, "2024-01-05 08:30:00"),
    Transaction("PURCHASED", "CompanyC", 100.0, "2024-01-12 13:00:00")
]


class CashbackCalculator:
    def __init__(self, transactions):
        self.transactions = transactions
        self.cashback_data = {}
    
    def process_transacitons(self):
        for transaction in transactions:
            if transaction.date not in self.cashback_data:
                self.cashback_data[transaction.date] = {}
            if transaction.company not in transaction.date:
                self.cashback_data[transaction.date][transaction.company] = 0.0
        self.cashback_data[transaction.date][transaction.company] += transaction.amount

    def top_n_transactions(self, n, month):
        #getting top n transactions for a given month
        if month not in self.cashback_data:
            return []
        company_cashbacks = self.cashback_data[month]
        sorted_cashbacks = sorted(company_cashbacks)
        return sorted_cashbacks[:n]