import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from AppTwo.models import Users
from faker import Faker

fake = Faker()

def populate(N=10):
    for pop in range(N):
        first_fake = fake.name()
        last_fake = fake.name()
        mails = fake.email()

        use = Users.objects.get_or_create(first_name=first_fake,
        last_name=last_fake,email=mails)[0]

if __name__ == '__main__':
    print('populating scripts')
    populate()
    print('population success')
