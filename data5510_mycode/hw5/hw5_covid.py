
import requests
import json
import csv

DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"


state_results = {}

populations = {}

with open("/workspaces/data5510_mycode/data5510_mycode/hw5/states.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        state = row[0].strip()
        population = int(row[1].strip())

        populations[state] = population

for state in populations:

    params = {
        "$where": f"state='{state}' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
        "$order": "end_date ASC",
        "$limit": 5000
    }

    # Retrieve data from API
    req = requests.get(BASE_URL, params=params)

    data = req.json()

    # Save data
    with open(f"/workspaces/data5510_mycode/data5510_mycode/hw5/{state}.json", "w") as file:
        json.dump(data, file, indent=4)


    total_cases = 0
    highest_cases = 0
    highest_date = ""
    monthly_cases = {}

    for record in data:

        new_cases = int(float(record.get("new_cases") or 0))
        end_date = record["end_date"]

        total_cases += new_cases

        # This is getting highest case
        if new_cases > highest_cases:
            highest_cases = new_cases
            highest_date = end_date

        # Get month and year
        month_year = end_date[:7]

        if month_year not in monthly_cases:
            monthly_cases[month_year] = 0

        monthly_cases[month_year] += new_cases

    # Calculate average
    average_cases = total_cases / len(data)

    # Find month with highest total cases
    highest_month = max(monthly_cases, key=monthly_cases.get)
    highest_month_cases = monthly_cases[highest_month]

    # Find population percentage
    population = populations[state]
    percentage = (highest_month_cases / population) * 100

    month_name = highest_month[5:7]
    year = highest_month[:4]

    month_name = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }[month_name]

    # Store results 
    state_results[state] = {
        "average": average_cases,
        "highest_date": highest_date,
        "highest_cases": highest_cases,
        "highest_month": f"{month_name} {year}",
        "monthly_cases": highest_month_cases,
        "percentage": percentage,
        "population": population
    }

    # Print results
    print(f"\nState name: {state}")
    print(f"Average number of new weekly cases for the entire state dataset: {average_cases:.2f}")
    print(f"Date with the highest new number of covid cases: {highest_date} ({highest_cases})")
    print(f"Month and Year, with the highest new number of covid cases: {month_name} {year} ({highest_month_cases})")
    print(f"Month and Year, with highest new number, percentage of population: {percentage:.2f}% (Population: {population})")


# Find Highest and Lowest Summarys
highest_state = max(state_results, key=lambda x: state_results[x]["percentage"])
lowest_state = min(state_results, key=lambda x: state_results[x]["percentage"])

highest = state_results[highest_state]
lowest = state_results[lowest_state]

# Print Summary

print("\nState with highest percentage of population during its highest month:")
print(f"{highest_state} - {highest['percentage']:.2f}% in {highest['highest_month']} ({highest['monthly_cases']} cases; Population: {highest['population']})")

print("\nState with lowest percentage of population during its highest month:")
print(f"{lowest_state} - {lowest['percentage']:.2f}% in {lowest['highest_month']} ({lowest['monthly_cases']} cases; Population: {lowest['population']})")