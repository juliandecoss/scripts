from faker import Faker
from datetime import datetime
faker = Faker()

def generate_event():
    return {
                "user_id": faker.pyint(100, 10000),
                "natural_person_id": faker.pyint(100, 10000),
                "enterprise_id": faker.pyint(100, 10000),
                "source": faker.word(),
                "email": faker.email(),
                "phone": faker.phone_number(),
                "first_name": faker.first_name(),
                "last_name": faker.last_name_male(),
                "last_name1": faker.last_name_male(),
                "last_name2": faker.last_name_female(),
                "enterprise_customer_type": "",
                "timestamp": datetime.now().isoformat(),
                "screen": "https://konfio.mx/mi/login",
                "utm_source": "",
                "utm_medium": "",
                "utm_campaign": "",
                "utm_term": "",
                "utm_content": "",
                "domain": "",
                "stage": "",
                "action": "",
        }