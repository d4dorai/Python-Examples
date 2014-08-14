import json
import sys

hashtag_counts = {}       # hashtag-count pair

# "entities":{
#  "hashtags":[
#         {
#         "text":"confused"
#     }
#  ],
def analyze_tweet(tweet):
    if not tweet: return
    if not 'entities' in tweet: return
    if not 'hashtags' in tweet['entities'] and len(tweet['entities']['hashtags']) == 0: return

    hashtags = tweet['entities']['hashtags']
    for hashtag_obj in hashtags:
        hashtag = hashtag_obj['text']
        occurrence = hashtag_counts.get(hashtag, 1)
        if hashtag in hashtag_counts:
            occurrence += 1
        hashtag_counts[hashtag] = occurrence

def analyze_tweets(tweet_file):
    for line in tweet_file:
        tweet = json.loads(line)
        analyze_tweet(tweet)

def print_results():
    for hashtag, count in sorted(hashtag_counts.items(), lambda x, y: cmp(y[1], x[1]))[:10]:
        print '%s %.1f' % (hashtag, count)


def hw(tweet_file):
    """ computes the ten most frequently occurring hash tags """
    analyze_tweets(tweet_file)
    print_results()

def main():
    tweet_file = open(sys.argv[1])
    # print tweet_file
    hw(tweet_file)

if __name__ == '__main__':
    main()
