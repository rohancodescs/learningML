class Transaction:
    def __init__(self, buyStatus, company, amount, date):
        self.company = company
        self.date = date
        if buyStatus == "PURCHASED" or buyStatus == "REFUNDED":
            self.buyStatus = buyStatus
        if buyStatus == "REFUNDED":
            self.amount = -abs(amount)
    def __str__(self):
        return f"Transaction: {[self.buyStatus, self.company, self.amount, self.date]}"

    def groupTransactions(transactions):
        hashmap = {}
        #ask can dates repeat?
        for buyStatus, company, amount, date in transactions:
            hashmap[date] = [company, amount]
        print(hashmap)
# import datetime
transactions = [
    ["PURCHASED", "CompanyA", 100.0, "2023-01-15 10:00:00"],
    ["PURCHASED", "CompanyB", 200.0, "2023-01-20 12:30:00"],
    ["REFUNDED", "CompanyA", 50.0, "2023-01-25 15:45:00"],
    ["PURCHASED", "CompanyC", 300.0, "2023-02-05 09:20:00"],
    ["PURCHASED", "CompanyA", 250.0, "2023-02-10 11:15:00"],
    ["REFUNDED", "CompanyB", 100.0, "2023-02-15 14:50:00"],
    ["PURCHASED", "CompanyB", 150.0, "2024-01-05 08:30:00"],
    ["PURCHASED", "CompanyC", 100.0, "2024-01-12 13:00:00"]
]
