from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.name(), #+ " " + faker_ru.last_name + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permonent_address=faker_ru.address(),
    )
