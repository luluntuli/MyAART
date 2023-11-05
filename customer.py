import requests
import csv

# Define the API endpoint
api_endpoint = "http://localhost:4000/flights?date=2023-10-21"

# Make a request to the API endpoint
response = requests.get(api_endpoint)

# Check if the request was successful
if response.status_code == 200:

    # Parse the API response into a JSON object
    data = response.json()

    # Open a CSV file for writing
    with open("data.csv", "w", newline="") as csvfile:

        # Create a CSV writer object
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(data[0].keys())

        # Write each row of data to the CSV file
        for row in data:
            writer.writerow(row.values())

# If the request was not successful, print an error message
else:
    print("Error: Could not fetch data from API")
