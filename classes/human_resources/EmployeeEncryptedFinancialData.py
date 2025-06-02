class EmployeeEncryptedFinancialData:
    def __init__(self, employeeId, clueHowToDecrypt, payRate, historyOfRaises, routingNumber, accountNumber): 
        self.employeeId = employeeId # must match the id of an instance of `Employee` 
        self.clueHowToDecrypt = clueHowToDecrypt
        self.payRate = payRate
        self.historyOfRaises = historyOfRaises
        self.routingNumber = routingNumber
        self.accountNumber = accountNumber
