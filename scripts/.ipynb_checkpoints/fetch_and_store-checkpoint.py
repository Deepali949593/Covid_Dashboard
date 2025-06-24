import requests
import pymongo
from datetime import datetime

# MongoDB connection string
MONGO_URI = "mongodb://localhost:27017"  # Or use your Atlas URI

client = pymongo.MongoClient(MONGO_URI)
db = client["covidDB"]
collection = db["covidData"]

def fetch_and_store():
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for record in data:
            record["fetchedAt"] = datetime.utcnow()
        collection.insert_many(data)
        print(f"Inserted {len(data)} records into MongoDB.")
    else:
        print("Failed to fetch data:", response.status_code)

if __name__ == "__main__":
    fetch_and_store()
