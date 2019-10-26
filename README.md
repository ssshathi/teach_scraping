# teach_scraping
Repository to teach how to scrape Twitter using the premium search API

## Instructions to download code:
1) Click the 'Clone or Download option
2) Click download zip
3) Unzip

## Setting up credentials
Modify the .twitter_keys.yaml file to contain your consumer key, consumer key secret, and desired endpoint
For example if your consumer key is **abcd**, your consumer secret is **efgh**, and the name of your dev environemnt is **dev_name**
your .yaml file will look like:

search_tweets_api:
  account_type: premium
  endpoint: https://api.twitter.com/1.1/tweets/search/fullarchive/dev_name.json
  consumer_key: abcd
  consumer_secret: efgh
  
 ## Installing packages
 Install the packages pandas and search-tweets 
 
 ## Run the code
 After you run the code, the data will be in twitter_data.tsv. Note that the code might take some time to run
