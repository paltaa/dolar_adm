# API Dolar Price

API that scraps dolar prices from sii's site.
Returns the value of dolar given a date and an amount in clp or usd, writen in python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to install django, django api rest framework and BeautifulSoup for scraping.



#### Installing

```
pip install djangorestframework
git clone -https://github.com/paltaa/dolar_adm.git
```
cd to directory and run:
```
python manage.py migrate
python manage.py scrap
python manage.py runserver
```

App ready for testing.

for usd to clp make requests to:  
[GET:http://127.0.0.1:8000/clp?usd=XXXX&date=yyyymmdd ]  
for clp to usd make requests to:  
[GET:http://127.0.0.1:8000/usd?clp=XXXX&date=yyyymmdd ]
for all saved dolars:  
[GET:http://127.0.0.1:8000/dolar_list ]
