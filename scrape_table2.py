# 1. Import Libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

# 2. Connect to Webpage-URL
url = 'https://www.worldometers.info/world-population/'

# 3. Create an Object-Soup
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

# 4. Print complete HTML-content
# print(soup) (only needed for check after connecting to Webpage-URL)

# 5. Getting the data of the table
table = soup.find('table', {'class': 'table table-striped table-bordered table-hover table-condensed table-list'})

headers = []

# 6. Getting all <th>-tags of the table (column-headers)
for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)

# 7. Create a Pandas-Dataframe
df = pd.DataFrame(columns = headers)

# 8. Getting all <td>-tags of the table (data of each row for each column)
for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data

# 9. Print table
print(df)

# 10. Save Pandas-Dataframe (table) in csv-file
df.to_csv('World Population Forecast (2020-2050).csv')