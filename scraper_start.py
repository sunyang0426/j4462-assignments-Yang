import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

#Open file and CSV writer
outfile = open('countyresults.csv', 'w')
writer = csv.writer(outfile)

br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/PickaRace.aspx')

# Fill out the top form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
br.submit('ctl00$MainContent$btnElectionType')

# Fill out the bottom form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboRaces'] = ['750003269']
br.submit('ctl00$MainContent$btnCountyChange')

# Get HTML
html = br.response().read()

# Set up BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find table body
tbody = soup.find('table', {'id': 'MainContent_dgrdCountyRaceResults'})

# Find the rows & cells from the table
rows = tbody.find_all('tr')

for row in rows:

	header = [cell.text.encode('utf-8') for cell in row.find_all('th')]

	data = [cell.text.encode('utf-8') for cell in row.find_all('td')]

	writer.writerow(header)
	writer.writerow(data)