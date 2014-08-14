import json
import sys

all_terms_count = 0         # of occurrences of all terms in all tweets
term_occurrences = {}       # of occurrences of the term in all tweets

def analyze_tweet(tweet):
    if not 'text' in tweet: return

    global all_terms_count
    words = tweet['text'].split()
    for word in words:
        all_terms_count += 1
        occurrence = term_occurrences.get(word, 1)
        if word in term_occurrences:
            occurrence += 1
        term_occurrences[word] = occurrence

def analyze_tweets(tweet_file):
    for i, line in enumerate(tweet_file):
        if line:
            try:
                tweet = json.loads(line)
                analyze_tweet(tweet)
            except ValueError:
                print "Failed to decode line %i : %s" % (i, line)

def calc_freq(occurrence):
    return float(occurrence) / all_terms_count

def print_results():
    # print "All Terms count: %i" % all_terms_count
    # Finally print the unknown word sentiment
    for term, occurrence in term_occurrences.items():
        line = '%s %f' % (term, calc_freq(occurrence))
        sys.stdout.write(line.encode('utf-8'))
        sys.stdout.write('\n')


def hw(tweet_file):
    analyze_tweets(tweet_file)
    print_results()

def main():
    tweet_file = open(sys.argv[1])
    # print tweet_file
    hw(tweet_file)

if __name__ == '__main__':
    main()
