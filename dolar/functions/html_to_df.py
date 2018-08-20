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
