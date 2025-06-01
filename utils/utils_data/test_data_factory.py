from datetime import datetime
from pathlib import Path

from faker import Faker
import json

fake = Faker()

class TestDataFactory:

    @staticmethod
    def generate_repository_data(count=1):
        repository_data = []

        for _ in range(count):
            repository_data.append({
                'repository_name': fake.name(),
                'description': fake.sentence(),
                'gitignore_template': fake.word(ext_word_list=['None', 'Python', 'Java'])
            })

        return repository_data

    @staticmethod
    def save_to_file(data, filename):
        Path("test_data").mkdir(exist_ok=True)

        filepath = Path("test_data") / filename

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def generate_all_test_data(save_data=False):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        data = {
            'repository_data': TestDataFactory.generate_repository_data(),
            'metadata': {
                'generated_at': timestamp,
                'faker_seed': Faker.seed(42)
            }
        }
        if save_data:
            TestDataFactory.save_to_file(data, filename=f'test_data_{timestamp}.json')

        return data