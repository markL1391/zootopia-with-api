import os
import requests
from dotenv import load_dotenv

# Load enviroment variables from .env file.
load_dotenv()

# Base URL of the API Ninjas animals endpoint.
BASE_URL = "https://api.api-ninjas.com/v1/animals"
# Read API key from environment variables.
API_KEY = os.getenv("API_KEY")

def fetch_data(animal_name: str):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  # Send GET request to the API.
  response = requests.get(
      BASE_URL,
      params={"name": animal_name},
      headers={"X-Api-Key": API_KEY}
  )

  # Check for unsuccessful HTTP response
  if response.status_code != 200:
      raise RuntimeError(
          f"API request failed: {response.status_code} {response.text}"
      )

  # Parse JSON response
  data = response.json()

  return data