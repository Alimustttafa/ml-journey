# Day 3: Data Aggregation with GROUP BY and COUNT

Today, I moved to Lesson 3 on Kaggle to learn how to group data and calculate aggregate metrics.

## What I learned:
- `GROUP BY`: Groups rows that have the same values into summary rows.
- Aggregate Functions: Used alongside GROUP BY to calculate statistics (like `COUNT`, `SUM`, `AVG`).

- Exercise:
The dataset used in this exercise is: >> Hacker News <<

Test(1):
1) Prolific commenters
Hacker News would like to send awards to everyone who has written more than 10,000 posts. Write a query that returns all authors with more than 10,000 posts as well as their post counts. Call the column with post counts NumPosts.
the code:
prolific_commenters_query = """
                            SELECT `by` AS author, COUNT(1) AS NumPosts
                            FROM `bigquery-public-data.hacker_news.full`
                            GROUP BY author
                            HAVING COUNT(1) > 10000
                            """ 
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
query_job = client.query(prolific_commenters_query, job_config=safe_config)

prolific_commenters = query_job.to_dataframe()

# View top few rows of results
print(prolific_commenters.head())


Test(2):
2) Deleted comments
How many comments have been deleted? (If a comment was deleted, the deleted column in the table will have the value True.)

the code:
deleted_posts = """
                select count(1) as deleted_posts
                from `bigquery-public-data.hacker_news.full`
                where deleted = true
                """

query_job = client.query(deleted_posts)

# API request - run the query, and return a pandas DataFrame
deleted_post = query_job.to_dataframe()

# View results
print(deleted_post)
