

import pandas as pd
import csv
import mysql.connectorcode co

# # Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="projectportfolio",
    auth_plugin=''  
)
query = "SELECT location, TotalPopulation, PopulationDensity, InfectionRate, DeathRate, DiabetesPrevelance, SmokerRate, CardioVascDeaRate, GDP_Per_Capita, AverageAge FROM CountryInfectionDeathStats"

# Execute the query
cursor = connection.cursor()
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Define the CSV file path
csv_file_path = 'C:/Users/arytn/OneDrive/Documents/Dance Data/SQL_Projects/countrycovidstats.csv'

# Write results to a CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header
    header = [i[0] for i in cursor.description]
    csv_writer.writerow(header)
    
    # Write the data
    csv_writer.writerows(results)

# Close the cursor and connection
cursor.close()
connection.close()
