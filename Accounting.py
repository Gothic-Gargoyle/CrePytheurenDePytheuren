class Administration:
    def __init__(self, name):
        self.name = name
        self.ledgers = [] # misscihen toch beter een dict van maken? {id - naam,object}

    def add_ledger(self, ledger):
        self.ledgers.append(ledger)

    def remove_ledger(self, ledger):
        self.ledgers.remove(ledger)

    def __str__(self):
        return self.name

    def get_administration_name(self):
        return self.name

    def get_ledgers(self):
        return self.ledgers

    def get_ledger(self,ledger_id):
        ...

class Ledger:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.entries = []
        self.relations = []

    def __str__(self):
        return f"{self.number} - {self.name}"

    def add_journalentry(self, entry):
        self.entries.append(entry)

    def remove_journalentry(self, entry):
        self.entries.remove(entry)

    def add_relation(self, relation):
        self.relations.append(relation)

    def remove_relation(self, relation):
        self.relations.remove(relation)

    def get_ledger_name(self):
        return self.name

    def get_relations(self):
        return self.relations

    def get_entries(self):
        return self.entries


class Relation(Ledger):
    def __init__(self, number, name):
        super().__init__(number, name)
        # voeg details als banken enzo later toe.


class Journalentry:
    def __init__(self, ledger, relation, bookdate, amount, cod, vat, description):
        self.ledger = ledger
        self.id = bookdate + ledger  # voeg hier nog een counter bij
        self.relation = relation
        self.bookdate = bookdate
        self.period = bookdate  # doe hier wat mee, periode berekenen
        self.amount = amount
        self.cod = cod  # geen true of false, wss iets van een enum? iig kiezen uit twee dingen
        self.vat = vat  # hier evenzo!
        self.description = description

    def __str__(self):
        return self.id


administratie = Administration("Cleopatra")
administratie.add_ledger(Ledger(1101, "tussenrekening"))

for items in administratie.get_ledgers():
    print(items)
