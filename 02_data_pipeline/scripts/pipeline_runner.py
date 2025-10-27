from extract_prescriptions import extract_new_data
from transform_load import transform, load_to_snowflake

def run_pipeline():
       raw_data = extract_new_data("http://127.0.0.1:5000/prescriptions")
       df = transform(raw_data)
       load_to_snowflake(df)
       print("Pipeline completed ✅")

if __name__ == "__main__":
       run_pipeline()