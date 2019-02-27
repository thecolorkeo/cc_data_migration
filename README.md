# cc_data_migration
This is my solution to Insight's "data_migration" coding challenge.

# Challenge
Create an ETL (Extract, Transform, Load) so that API data is consumable by business analysts. Fortunately, your co-workers have already done the Extract step and has provided you with a .zip file containing retail order data in the raw JSON format. Your project manager has put you on the task to support these business analysts so that they can query that data using SQL from a PSQL database. While you’re at it, they would also want you to create a user table that would contain summary metrics that you think business analysts would find useful. Keep in mind that the newly created tables have to be sanely structured and those steps should be reproducible with the expectation that the ETL would run daily. For full instructions, see [instructions](https://github.com/Samariya57/coding_challenges/blob/master/data_migration.md).

# Input file
`data/data.zip`
Collection of zipped json files. Each file is laid out as follows:
```
{
  "orders": [
    {
      "id": 11748933635,
      "email": "censored@censored.com",
      "closed_at": null,
      "created_at": "2017-10-30T19:58:29-04:00",
      "updated_at": "2017-10-30T19:59:30-04:00",
      "number": 97171,
      "note": null,
      "token": "censored",
      "gateway": "cash",
      "test": false,
      "total_price": "130.64999999999998",
...
      "line_items": [
        {
          "id": 23495245827,
          "variant_id": 36499702851,
          "quantity": 1,
          "product_id": 9096535107
        }
      ],
      "total_discount": null
    },
  ]
}
```

# Solution
First, I unzip json files into the unzipped folder. After that, I read them in and combine them into a single dataframe. I write that dataframe into Postgres. My program takes 2 arguments, which are the path to the zipped files (should be `/data/data.zip`) and the output folder (`/unzipped`).

After the table is written, I calculate a summary statistics table off of it with `summary_stats.py`. At the moment, the only stat calculated is the average price paid per transaction for each userid. This could be expanded to other statistics of choice.

# Run
Run with `/run.sh` from the root directory.
