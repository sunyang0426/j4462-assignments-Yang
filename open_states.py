# 1. List all legislators in Missouri who are currently active lawmakers.
#   http://openstates.org/api/v1/legislators/?state=mo&active=true

# 2. List all of the bills introduced in the Missouri Senate during the 2016 session.
#   http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&chamber=upper

# 3. Further filter the previous list to include only bills related to a subject of your choice.
#  http://http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&chamber=upper&q=Health

# 4. Write some code that, for every bill in the list from Question 3, prints its name and the most recent action taken on it. Hint: This might involve using more than one endpoint.


import json, requests

url = 'http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&chamber=upper&q=Health'

r = requests.get(url)

data = json.loads(r.content)

for item in data:
	print item['title']
	print item['updated_at']

