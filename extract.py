import requests

url = "https://www.fema.gov/api/open/v2/PublicAssistanceFundedProjectsDetails"

api_data = requests.get(url)

api_data.json()

print(api_data.json()['PublicAssistanceFundedProjectsDetails'])


