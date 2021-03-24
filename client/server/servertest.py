from dbclass import PostGreSQL
import string
import random

db = PostGreSQL()

def random_data():
    letters = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    r1 = random.randint(10, 99)
    data = [letters, r1]
    return data


def populate_db(table: str):
    data = random_data()
    db.insert(table, data)


# Loop and populate the db with 10 entries
# for i in range(10):
#   populate_db("score")

db.select("score")
