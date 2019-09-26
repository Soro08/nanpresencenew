from django_faker import Faker
# this Populator is only a function thats return a django_faker.populator.Populator instance
# correctly initialized with a faker.generator.Generator instance, configured as above
populator = Faker.getPopulator()

from presence.models import *
populator.addEntity(Jours_cours,5)

insertedPks = populator.execute()