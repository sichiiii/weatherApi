from csv import DictReader
from django.core.management import BaseCommand

from ...models import City


class Command(BaseCommand):
    help = "Loads data from cities_lat_lon.csv"

    def handle(self, *args, **options):
        if City.objects.exists():
            print('Data already loaded...exiting.')
            return

        print("Loading data...")

        for row in DictReader(open('./cities_lat_lon.csv')):
            city = City(name=row['city'], latitude=row['lat'], longitude=row['lon'])
            city.save()