from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from dateutil import parser
from dolar.models import Dolar
from scraper import html_to_df


class Command(BaseCommand):

    help= 'Scraps the data from SIIs site from 1990 to current date'

    def handle(self, *args, **options):
        exec(open('scraper.py').read())
