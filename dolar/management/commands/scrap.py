from django.core.management.base import BaseCommand, CommandError
from dolar.models import Dolar
from dolar.functions.scraper import scraper
from django.shortcuts import get_object_or_404

class Command(BaseCommand):

    help= 'Scraps the data from SIIs site from 1990 to current date'

    def handle(self, *args, **options):
        #exec(open('scraper.py').read())
        for year in range(1990,2019):
            dolar_year=scraper(year)
            for tuples in dolar_year:
                dolar=Dolar(date=tuples[0], value=tuples[1])
                try:
                    dlr=Dolar.objects.get(date=tuples[0])
                except:
                    dlr=None
                if( dlr == None):
                    try:
                        dolar.save()
                    except:
                        print('Saving error ocurred')
                    else:
                        print (tuples)
                        print ('Saved')
                else:
                    print ('Value already saved for date {}'.format(tuples[0]))
