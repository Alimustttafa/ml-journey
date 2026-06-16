# Day 2: Mastering SELECT, FROM, and AS in SQL

Today, I wrote my first functional SQL queries to retrieve specific data from tables.

## What I learned:
- `SELECT`: Used to specify which columns to retrieve (or `*` for all columns).
- `FROM`: Used to specify the table name.
- `AS`: Used to create an alias (rename a column temporarily for better readability).

Exercise:
from google.cloud import bigquery

# Initialize the client
client = bigquery.Client()

# Constructing a safe, filtered query
query = """
        SELECT score, title
        FROM `bigquery-public-data.hacker_news.full`
        WHERE type = "job"
        """

# Enforcing a 1 GB maximum limit for safety
ONE_GB = 1000 * 1000 * 1000
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=ONE_GB)

# Execute safely
query_job = client.query(query, job_config=safe_config)
results_df = query_job.to_dataframe()

# Inspecting top value counts
print(results_df.head())
