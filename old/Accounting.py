class Administration:
    def __init__(self,admin_id, name):
        self.admin_id= admin_id
        self.name = name
        self.bookyears = []
        self.ledgers = []  # misscihen toch beter een dict van maken? {id - naam,object}
        # [{id- naam, object},etc}

    def __str__(self):
        return self.name

    def add_bookyear(self, year):
        period = tuple(f"{year}/{i}" for i in range(0, 13))
        self.bookyears.append((year, period))  # voegt periodes toe, die dan weer nodig zijn om iets te boeken.

    def add_ledger(self, ledger):
        self.ledgers.append(ledger)

    def remove_ledger(self, ledger):
        self.ledgers.remove(ledger)

    def get_administration_name(self):
        return self.name

    def get_ledgers(self):
        return self.ledgers

    def get_ledger(self, ledger_id):
        for l in self.ledgers:
            if l == ledger_id:
                return l


class Ledger:
    def __init__(self, ledger_id, name):
        self.ledger_id = ledger_id
        self.name = name
        self.entries = []
        self.relations = []

    def __str__(self):
        return f"{self.ledger_id} - {self.name}"

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
    def __init__(self, number, name, iban):
        super().__init__(number, name)
        # voeg details als banken enzo later toe.
        self.iban = iban


class Journalentry:
    def __init__(self, ledger, relation, bookdate, amount, cod, vat, description, state):
        self.ledger = ledger
        self.journal_id = bookdate + ledger  # voeg hier nog een counter bij
        self.relation = relation
        self.bookdate = bookdate
        self.period = bookdate  # doe hier wat mee, periode berekenen, ook boekjaren inbouwen! state pattern! Concept, definitief,afgeletterd
        self.amount = amount
        self.cod = cod  # geen true of false, wss iets van een enum? iig kiezen uit twee dingen
        self.vat = vat  # hier evenzo!
        self.description = description
        self.state = ...  # state pattern! Concept, definitief,afgeletterd

    # TODO Uitzoeken hoe splitsen/verdelen van boekingen (part to whole) te controleren (View?)

    def __str__(self):
        return self.journal_id


administratie = Administration(1, "Cleopatra")
administratie.add_ledger(Ledger(1101, "tussenrekening"))
administratie.add_ledger(Ledger(1104, "tussenrekening Storneren"))
administratie.add_ledger(Ledger(4104, "Hobbies"))
administratie.add_ledger(Ledger(8104, "Hobbies"))

for items in administratie.get_ledgers():
    print(items)
