import mysql.connector
import csv
from datetime import datetime


# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="projectportfolio",
    auth_plugin='password'  # Use the compatible authentication method

)

cursor = db.cursor()


# List of column names
# columns = [
#     'iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases',
#     'total_deaths', 'new_deaths', 'new_deaths_smoothed',
#     'total_cases_per_million', 'new_cases_per_million', 'new_cases_smoothed_per_million',
#     'total_deaths_per_million', 'new_deaths_per_million', 'new_deaths_smoothed_per_million',
#     'reproduction_rate', 'icu_patients', 'icu_patients_per_million', 'hosp_patients',
#     'hosp_patients_per_million', 'weekly_icu_admissions', 'weekly_icu_admissions_per_million',
#     'weekly_hosp_admissions', 'weekly_hosp_admissions_per_million', 'new_tests', 'total_tests',
#     'total_tests_per_thousand', 'new_tests_per_thousand', 'new_tests_smoothed',
#     'new_tests_smoothed_per_thousand', 'positive_rate', 'tests_per_case', 'tests_units',
#     'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'new_vaccinations',
#     'new_vaccinations_smoothed', 'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
#     'people_fully_vaccinated_per_hundred', 'new_vaccinations_smoothed_per_million', 'stringency_index',
#     'population', 'population_density', 'median_age', 'aged_65_older', 'aged_70_older',
#     'gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate', 'diabetes_prevalence',
#     'female_smokers', 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
#     'life_expectancy', 'human_development_index'
# ]

columns = ['iso_code', 'continent', 'location', 'date', 'new_tests', 'total_tests',
       'total_tests_per_thousand', 'new_tests_per_thousand',
       'new_tests_smoothed', 'new_tests_smoothed_per_thousand',
       'positive_rate', 'tests_per_case', 'tests_units', 'total_vaccinations',
       'people_vaccinated', 'people_fully_vaccinated', 'new_vaccinations',
       'new_vaccinations_smoothed', 'total_vaccinations_per_hundred',
       'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred',
       'new_vaccinations_smoothed_per_million', 'stringency_index',
       'population_density', 'median_age', 'aged_65_older', 'aged_70_older',
       'gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate',
       'diabetes_prevalence', 'female_smokers', 'male_smokers',
       'handwashing_facilities', 'hospital_beds_per_thousand',
       'life_expectancy', 'human_development_index'
]


# Generate the SQL INSERT statement string
columns_str = ', '.join(columns)
values_str = ', '.join(['%s'] * len(columns))

insert_sql = f"INSERT INTO covidvaccinations ({columns_str}) VALUES ({values_str})"


csv_file = "CovidVaccinations2.csv"

# Read and insert data
with open(csv_file, newline='') as file:
    csv_data = csv.reader(file, delimiter=',')
    next(csv_data)  # Skip the header row if necessary

    for row in csv_data:
        # Convert the 'date' column from 'MM/DD/YYYY' to 'YYYY-MM-DD' format
        date_str = row[3]  # Assuming 'date' is in the 4th position (0-based index)
        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
        row[3] = date_obj.strftime('%Y-%m-%d')

        # Handle empty values by converting them to None (NULL in MySQL)
        for i in range(len(row)):
            if row[i] == '':
                row[i] = None

        # Execute the INSERT statement
        cursor.execute(insert_sql, row)

db.commit()
db.close()
