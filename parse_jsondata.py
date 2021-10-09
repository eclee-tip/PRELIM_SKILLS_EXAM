import json #Importing the json library
import csv #Importing the csv library

with open('/home/devasc/CPE41S1/prelim_skills_lee/covid_cases.json', 'r') as data_covid: #Reading the json file
    covid_data = json.loads(data_covid.read()) #Loads the json file

with open('/home/devasc/CPE41S1/prelim_skills_lee/json_parsed.csv', 'w', newline='') as json_parsed: #Saving to csv file
    csv_file = csv.writer(json_parsed)
    csv_file.writerow(["dateRep", "countriesAndTerritories", "cases", "deaths"]) #Assigns the values

    for data in covid_data["records"]: #Looping the data that will be recoded to the csv file
        csv_file.writerow([data["dateRep"], 
        data["countriesAndTerritories"], 
        data["cases"], 
        data["deaths"]])


