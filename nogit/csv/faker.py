from faker import Faker
faker = Faker()
Faker.seed(0)
print(faker.phone_number())