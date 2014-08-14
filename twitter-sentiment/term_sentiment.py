import json
import sys


all_unknown_terms = {}

def analyze_tweet(tweet, scores):
    # print '[>>>>] analyzing tweet...'
    # print '[text] %s' % tweet

    words = tweet['text'].split(' ')

    unknown_words = []

    # calculate the score
    tweet_score = 0
    for word in words:
        if word in scores:
            word_score = scores[word]
            # print "%s:%i" % (word, word_score)
            tweet_score += word_score
        else:
            unknown_words.append(word)

    for unknown_word in unknown_words:
        if unknown_word in all_unknown_terms:
            all_unknown_terms[unknown_word].append(tweet_score)
        else:
            all_unknown_terms[unknown_word] = [tweet_score]


def analyze_tweets(tweet_file, scores):

    for line in tweet_file:
        tweet = json.loads(line)
        analyze_tweet(tweet, scores)

def print_results():

    # Finally print the unknown word sentiment
    for unknown_word, scores in all_unknown_terms.items():
        sentiment = float(sum(scores) / len(scores))
        print '%s %.2f' % (unknown_word, sentiment)


def hw(sent_file, tweet_file):
    scores = create_sentiment_score_dict(sent_file)
    analyze_tweets(tweet_file, scores)
    print_results()

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
