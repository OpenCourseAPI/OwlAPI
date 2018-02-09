from tinydb import TinyDB

class TinyTable():
    def __init__(self, db):
        self.db = db

    def get_table(self, name):
        if name in self.db._table_cache:
            return self.db._table_cache[name]