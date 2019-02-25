# cc_data_migration
This is my solution to Insight's "data_migration" coding challenge.

# Challenge
Create an ETL (Extract, Transform, Load) so that API data is consumable by business analysts. Fortunately, your co-workers have already done the Extract step and has provided you with a .zip file containing retail order data in the raw JSON format. Your project manager has put you on the task to support these business analysts so that they can query that data using SQL from a PSQL database. While you’re at it, they would also want you to create a user table that would contain summary metrics that you think business analysts would find useful. Keep in mind that the newly created tables have to be sanely structured and those steps should be reproducible with the expectation that the ETL would run daily. For full instructions, see (instructions)[https://github.com/Samariya57/coding_challenges/blob/master/data_migration.md]

# Input file
`data/data.zip`
Collection of zipped json files.

# Solution
First, I unzip json files into the unzipped folder. After that, I read them in and combine them into a single dataframe. I write that dataframe into Postgres. My program takes 2 arguments, which are the path to the zipped files (should be `/data/data.zip`) and the output folder (`/unzipped`).

# Run
Run with run.sh from the root directory.
