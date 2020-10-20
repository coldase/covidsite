import requests
import json

#returns data as dict
def get_data(country):
	url = "https://corona.lmao.ninja/v3/covid-19/countries/" + str(country.lower())
	res = requests.get(url, 
		headers={"Accept":"application/json"})
 
	return json.loads(res.text)