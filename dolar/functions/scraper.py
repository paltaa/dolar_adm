from urllib.request import urlopen
from bs4 import BeautifulSoup
from dateutil import parser
import pandas as pd


def scraper(year):
    year_str=str(year)
    if ( year >=  2013):
        html_doc= "http://www.sii.cl/valores_y_fechas/dolar/dolar"+year_str+".htm#"
    elif(year >= 1990 and year < 2013):
        html_doc= "http://www.sii.cl/pagina/valores/dolar/dolar"+year_str+".htm"
    url = urlopen(html_doc)
    with url as fp:
        soup = BeautifulSoup(fp)
    if ( year >=  2013):
        table = soup.find("div", {"id": "mes_all"}, {"id": "table export"})
    elif(year >= 1990 and year < 2013):
        table= soup.find("div", {"id": "contenido"})
    new_table = html_to_df( table )
    days , months = new_table.shape
    dolarByDate=list()
    for month in range(1,months):
        for day in range(1,days):
            value=new_table.iloc[day][month].replace(',','.')
            if(value != '' and value != '>\xa0' and value !='\xa0' ):
                date=parser.parse(year_str+'-'+str(month)+'-'+str(day))
                value=float(value)
                dolarByDate.append((date, value))
    return dolarByDate

def html_to_df( table ):
    new_table = pd.DataFrame(columns=range(0,13), index= range(0,32))
    row_marker = 0
    for row in table.find_all('tr'):
        column_marker = 0
        columns = row.find_all('td')
        for column in columns:
            new_table.iat[row_marker,column_marker+1] = column.get_text()
            column_marker += 1
        row_marker += 1
        if(row_marker==32):
            break
    return new_table
