import json
import sys

states = {
    'AK': 0,
    'AL': 0,
    'AR': 0,
    'AS': 0,
    'AZ': 0,
    'CA': 0,
    'CO': 0,
    'CT': 0,
    'DC': 0,
    'DE': 0,
    'FL': 0,
    'GA': 0,
    'GU': 0,
    'HI': 0,
    'IA': 0,
    'ID': 0,
    'IL': 0,
    'IN': 0,
    'KS': 0,
    'KY': 0,
    'LA': 0,
    'MA': 0,
    'MD': 0,
    'ME': 0,
    'MI': 0,
    'MN': 0,
    'MO': 0,
    'MP': 0,
    'MS': 0,
    'MT': 0,
    'NA': 0,
    'NC': 0,
    'ND': 0,
    'NE': 0,
    'NH': 0,
    'NJ': 0,
    'NM': 0,
    'NV': 0,
    'NY': 0,
    'OH': 0,
    'OK': 0,
    'OR': 0,
    'PA': 0,
    'PR': 0,
    'RI': 0,
    'SC': 0,
    'SD': 0,
    'TN': 0,
    'TX': 0,
    'UT': 0,
    'VA': 0,
    'VI': 0,
    'VT': 0,
    'WA': 0,
    'WI': 0,
    'WV': 0,
    'WY': 0,
}

def get_state(tweet):
    place = tweet['place']
    for state in states.iterkeys():
        if state in place['full_name']: return state

    return None


def is_from_us(tweet):
    # if 'coordinates' in tweet and tweet['coordinates']: return True # TODO
    # if 'geo' in tweet and tweet['geo']: return True # TODO
    place = tweet['place']
    if place:
        return place['country_code'] == 'US'

def can_analyze(tweet):
    return 'text' in tweet \
           and 'lang' in tweet \
           and tweet['lang'] == 'en' \
           and is_from_us(tweet)

def analyze(tweet, scores):
    if not can_analyze(tweet): return

    words = tweet['text'].split(' ')

    # calculate the score
    tweet_score = 0
    for word in words:
        if word in scores:
            word_score = scores[word]
            # print "%s:%i" % (word, word_score)
            tweet_score += word_score

    state = get_state(tweet)

    if state:
        states[state] += tweet_score
        # print '%s %.2f' % (state, float(tweet_score))

def analyze_tweets(tweet_file, scores):
    for line in tweet_file:
        tweet = json.loads(line)
        analyze(tweet, scores)

def print_result():
    print sorted(states.items(), lambda x, y: cmp(y[1], x[1]))[0][0]

def hw(sent_file, tweet_file):
    """
     returns the name of the happiest state as a string.
    """
    analyze_tweets(tweet_file, create_sentiment_score_dict(sent_file))
    print_result()

def create_sentiment_score_dict(sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # print scores.items() # Print every (term, score) pair in the dictionary
    return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
