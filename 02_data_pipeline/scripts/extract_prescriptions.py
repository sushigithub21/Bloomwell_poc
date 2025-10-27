import json
import requests

def extract_new_data(api_url):
       response = requests.get(api_url)
       data = response.json()
       return data

if __name__ == "__main__":
       prescriptions_data = extract_new_data("http://127.0.0.1:5000/prescriptions")
       print(f"Extracted {len(prescriptions_data)} prescriptions")