import requests
import json

#returns data as dict
def get_data(country):
	url = "https://corona.lmao.ninja/v3/covid-19/countries/" + str(country.lower())
	res = requests.get(url, 
		headers={"Accept":"application/json"})

	return json.loads(res.text)

#returns list of countries
def get_country():
	all_countries = []
	url = "https://corona.lmao.ninja/v3/covid-19/countries/"
	res = requests.get(url,
		headers={"Accept":"application/json"})

	for x in json.loads(res.text):
		all_countries.append(x["country"].lower())
	
	return all_countries
