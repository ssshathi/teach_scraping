from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results
import pandas as pd


premium_search_args = load_credentials('.twitter_keys.yaml', 'premium', 'search_tweets_api')
pt_rule = '#oscarsowhite lang:en' # the #oscarsowhite is the query, the lang:en is to filter it to only be english lang tweets
results_per_call = 500 # this is the max number of results you can get per call
from_date = '201501010000' # this is set to 01/01/2015, the format is YYYYMMDDMinMinSecSec
to_date = '201503010000' # this is set to 03/01/2015
max_results = 100000 # Set this to the total number of tweets you want. Note that there is maximum associated with the amount you pay.
# For the $224 one, the max you can get is 125,000

rule = gen_rule_payload(pt_rule, results_per_call=results_per_call, from_date=from_date, to_date=to_date)
tweets = collect_results(rule, max_results=max_results, result_stream_args=premium_search_args)

df = []
for i, tweet in enumerate(tweets):
    if i % 10000 == 0:
        print('processing tweet {}'.format(i))
    tweet_row = []
    tweet_row.append(tweet.all_text.replace('\n', ' ').replace('\t', ' '))
    tweet_row.append(tweet.hashtags)
    tweet_row.append(tweet.retweet_count)
    tweet_row.append(tweet.retweeted_tweet.text if tweet.retweeted_tweet else None)
    tweet_row.append(tweet.name)
    tweet_row.append(tweet.created_at_datetime)
    df.append(tweet_row)

df = pd.DataFrame(df, columns=['text', 'hashtags', 'retweet_count', 'retweeted_tweet', 'name', 'created_at'])
df.to_csv('twitter_data.tsv', sep='\t', index=None)