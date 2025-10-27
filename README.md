# Bloomwell Data Pipeline PoC

   Overview
   This proof of concept demonstrates a data pipeline that extracts prescription data from a mock API, transforms it, and simulates loading it into Snowflake.

   Structure
   - `config/`: Configuration files.
   - `data/`: Sample data files.
   - `scripts/`: Python scripts for extraction, transformation, and loading.
   - `sql/`: SQL scripts for table creation.

   How to Run
   1. Start the Flask API:
```bash
      python api.py
