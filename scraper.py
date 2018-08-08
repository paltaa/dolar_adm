from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


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

years = [
"2013",
"2014",
"2015",
"2016",
"2017",
"2018"
]
html_doc= "http://www.sii.cl/valores_y_fechas/dolar/dolar2015.htm#"
html_docb= "http://www.sii.cl/pagina/valores/dolar/dolar2010.htm"
url = urllib.request.urlopen(html_doc)
urlb= urllib.request.urlopen(html_docb)
with url as fp:
    soup = BeautifulSoup(fp)
with urlb as fp:
    soupb = BeautifulSoup(fp)

table = soup.find("div", {"id": "mes_all"}, {"id": "table export"})
tableb= soupb.find("div", {"id": "contenido"})


new_table = html_to_df( tableb )

print (new_table)
