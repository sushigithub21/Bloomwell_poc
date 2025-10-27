import pandas as pd
from datetime import datetime

def transform(raw_data):
       df = pd.DataFrame(raw_data)
       df['ingest_time'] = datetime.utcnow()
       return df

def load_to_snowflake(df):
       print("Simulating load to Snowflake:")
       print(df)

if __name__ == "__main__":
       from extract_prescriptions import extract_new_data
       raw = extract_new_data("http://127.0.0.1:5000/prescriptions")
       df = transform(raw)
       load_to_snowflake(df)