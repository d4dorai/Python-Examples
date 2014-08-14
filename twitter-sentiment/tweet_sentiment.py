import json
import sys

def analyze_tweet(tweet, scores):

    words = tweet['text'].split(' ')

    # calculate the score
    tweet_score = 0
    for word in words:
        if word in scores:
            word_score = scores[word]
            # print "%s:%i" % (word, word_score)
            tweet_score += word_score

    # Finally print the tweet sentiment
    print '%.2f' % float(tweet_score)

def analyze_tweets(tweet_file, scores):

    for line in tweet_file:
        tweet = json.loads(line)
        analyze_tweet(tweet, scores)


def hw(sent_file, tweet_file):
    """
     Compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet.
     The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.
    """
    scores = create_sentiment_score_dict(sent_file)
    # print "[ OK ] sentiment score dictionary has %i items." % len(scores.items())
    analyze_tweets(tweet_file, scores)

def create_sentiment_score_dict(sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # print scores.items() # Print every (term, score) pair in the dictionary
    return scores

def main():
    sent_file = open(sys.argv[1])
    # print sent_file
    tweet_file = open(sys.argv[2])
    # print tweet_file
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
