# Import the necessary libraries.
import requests
import json
# Define the base URL for the customer contact details API.
BASE_URL = "https://api.example.com/v1/customers/"
# Define the headers for the API request.
HEADERS = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
}
# Define the data for the API request.
DATA = {
    "name": "MS Anas",
    "email": "Anaslko786@.com",
    "phone": "9169961650",
}
# Make the API request.
response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(DATA))
# Check the response status code.
if response.status_code == 200:
    # The request was successful.
    print("Customer contact details successfully updated.")
else:
    # The request failed.
    print("Error updating customer contact details.")