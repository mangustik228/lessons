from pymongo.collection import Collection
from mimesis import Person


def generate_fake_data(collection: Collection, n: int = 5, print_: bool = False):
    faker = Person('ru')
    fake_data = [
        {
            "name": faker.first_name(),
            "surname": faker.surname(),
            "language": faker.language(),
            "age": faker.age()
        } for _ in range(n)
    ]
    collection.insert_many(fake_data)
    if print_:
        print(list(collection.find()))
