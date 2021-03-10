import datetime


class CreDebReg:
    def __init__(self):
        self.financialrecords = []

    def addEntity(self,record):
        self.financialrecords.append(record)

    def showReg(self):
        return self.financialrecords[:]


class FinancialEntity:
    def __init__(self, name, debt, invoicedate, invoiceexpirydate):
        self.name = name
        self.debt = debt
        self.invoicedate = invoicedate  # datum van factuur
        self.invoiceexpirydate = invoiceexpirydate  # vervaldatum van factuur
        self.invoiceterms = []  # aantal betaaltermijnen
        self.invoicepayedoff = False

    def decreaseDebt(self, amount):
        self.debt -= amount
        if self.debt == 0:
            self.invoicepayedoff = True

    def addInvoiceTerm(self, amount):
        debtleft = self.debt
        paydate = datetime.datetime.today()
        self.decreaseDebt(amount)
        self.invoiceterms.append((paydate, amount, debtleft))


class Crediteur(FinancialEntity):
    def __init__(self, name, debt, invoicedate, invoiceexpirydate):
        super().__init__(name, debt, invoicedate, invoiceexpirydate)


class Debiteur(FinancialEntity):
    def __init__(self, name, debt, invoicedate, invoiceexpirydate):
        super().__init__(name, debt, invoicedate, invoiceexpirydate)

testCDR = CreDebReg()
cred1 = Crediteur('cleopatra',101,'11-12-2019','11-2-2020')
testCDR.addEntity(cred1)
testCDR.showReg()