from database import Database


class Contact:
    db = Database()

    def __init__(self, id=None, name=None, phone=None):
        self.id = id
        self.name = name
        self.phone = phone

    @staticmethod
    def convert(records):
        return [
            Contact(id=record["id"], name=record["name"], phone=record["phone"])
            for record in records
        ]

    def save(self):
        query = (
            f"INSERT INTO {self.db.table} (name, phone) VALUES (%s, %s) RETURNING id"
        )
        results = self.db.execute(query, (self.name, self.phone))
        if results:
            self.id = results[0]["id"]
            return self.id
        else:
            return None

    def update(self):
        query = f"UPDATE {self.db.table} SET name = %s, phone = %s WHERE id = %s"
        results = self.db.execute(query, (self.name, self.phone, self.id))
        return self

    def destroy(self):
        self.db.execute(f"DELETE FROM {self.db.table} WHERE id =%s", (self.id))
        return self

    @classmethod
    def all(cls):
        results = cls.db.execute(f"SELECT * FROM {cls.db.table}")
        return cls.convert(results)

    @classmethod
    def find(cls, id):
        results = cls.db.execute(
            f"SELECT * FROM {cls.db.table} WHERE id=%s", (int(id),)
        )
        return cls.convert(results)

    @classmethod
    def findByNumber(cls, string):
        results = cls.db.execute(
            f"SELECT * FROM {cls.db.table} WHERE phone=%s", (string,)
        )
        return cls.convert(results)

    @classmethod
    def findByName(cls, string):
        results = cls.db.execute(
            f"SELECT * FROM {cls.db.table} WHERE name LIKE %s", (f"%{string}%",)
        )
        return cls.convert(results)
