# Day 5: Organizing Queries with CTEs (WITH ... AS)

Today, I learned how to create temporary result sets called Common Table Expressions (CTEs) to make complex queries cleaner and more readable.

## What I learned:
- `WITH ... AS`: Defines a temporary table that exists only during the execution of the query.
- It helps break down complex multi-step analysis into organized blocks.

- Exercise:
  The dataset name: Chicago Taxi Trips
- Test(1):
1) Determine when this data is from
If the data is sufficiently old, we might be careful before assuming the data is still relevant to traffic patterns today. Write a query that counts the number of trips in each year.

Your results should have two columns:

year - the year of the trips
num_trips - the number of trips in that year

- solution:
rides_per_year_query = """
                       select EXTRACT(YEAR FROM trip_start_timestamp) as year,
                               count(1) as num_trips
                       from `bigquery-public-data.chicago_taxi_trips.taxi_trips`
                       group by year
                       order by year
                       """


safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
rides_per_year_query_job = client.query(rides_per_year_query, job_config=safe_config)


rides_per_year_result = rides_per_year_query_job.to_dataframe()


print(rides_per_year_result)


-Test(2):
2) Dive slightly deeper
You'd like to take a closer look at rides from 2016. Copy the query you used above in rides_per_year_query into the cell below for rides_per_month_query. Then modify it in two ways:

Use a WHERE clause to limit the query to data from 2016.
Modify the query to extract the month rather than the year

- Solution:
rides_per_month_query = """
                       select EXTRACT(month FROM trip_start_timestamp) as month,
                               count(1) as num_trips
                       from `bigquery-public-data.chicago_taxi_trips.taxi_trips`
                       where extract(year from trip_start_timestamp) = 2016
                       group by month
                       order by month
                       """

safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
rides_per_month_query_job = client.query(rides_per_month_query, job_config=safe_config)

rides_per_month_result = rides_per_month_query_job.to_dataframe()

print(rides_per_month_result)

Test(3):
3) Write the query
It's time to step up the sophistication of your queries. Write a query that shows, for each hour of the day in the dataset, the corresponding number of trips and average speed.

Your results should have three columns:

hour_of_day - sort by this column, which holds the result of extracting the hour from trip_start_timestamp.
num_trips - the count of the total number of trips in each hour of the day (e.g. how many trips were started between 6AM and 7AM, independent of which day it occurred on).
avg_mph - the average speed, measured in miles per hour, for trips that started in that hour of the day. Average speed in miles per hour is calculated as 3600 * SUM(trip_miles) / SUM(trip_seconds). (The value 3600 is used to convert from seconds to hours.)
Restrict your query to data meeting the following criteria:

a trip_start_timestamp > 2016-01-01 and < 2016-04-01
trip_seconds > 0 and trip_miles > 0

-Solution:
speeds_query =  """
               WITH RelevantRides AS
               (
                   SELECT EXTRACT(HOUR FROM trip_start_timestamp) AS hour_of_day, 
                          trip_miles, 
                          trip_seconds
                   FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
                   WHERE trip_start_timestamp > '2016-01-01' AND 
                         trip_start_timestamp < '2016-04-01' AND 
                         trip_seconds > 0 AND 
                         trip_miles > 0
               )
                SELECT hour_of_day, 
                      COUNT(1) AS num_trips, 
                      3600 * SUM(trip_miles) / SUM(trip_seconds) AS avg_mph
               FROM RelevantRides
               GROUP BY hour_of_day
               ORDER BY hour_of_day
               """

safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
speeds_query_job = client.query(speeds_query, job_config=safe_config)


speeds_result = speeds_query_job.to_dataframe()

print(speeds_result)
