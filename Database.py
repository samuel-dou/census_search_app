import pymssql

class Database:
    __connection = None

    @classmethod
    def connect(cls):
        if cls.__connection is None:
            cls.__connection = pymssql.connect(
                server='cisdbss.pcc.edu',
                user='275student',
                password='275student',
                database='NAMES'
            )

    @classmethod
    def fetch_person(cls, name, gender):
        from Person import Person
        cls.connect()
        cursor = cls.__connection.cursor(as_dict=True)
        sql = """
                SELECT Name, Year, Gender, NameCount, Total
                FROM all_data
                WHERE Name = %s
                AND Gender = %s
                ORDER BY Year;
                """
        cursor.execute(sql, (name, gender))
        count = cursor.fetchall()
        persons = []
        for row in count:
            person = Person(name=row['Name'], year=row['Year'], gender=row['Gender'],
                         namecount=row['NameCount'], total=row['Total'])
            persons.append(person)
        return persons