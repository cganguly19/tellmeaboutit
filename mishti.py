# coding: utf-8


import random
from nltk.sentiment.vader import SentimentIntensityAnalyzer

inspirational_quotes = ['Listen, smile, agree and then do whatever you were going to do anyway.',             
              'Never let a bad day make you feel like you have a bad life.',
              'The person who says something is impossible should not interrupt the person who is doing it.', 
              'It is never too late to be what you might have been.',
              'Great minds discuss ideas. Average minds discuss events. Small minds discuss people.',
              'If opportunity doesn\’t knock, build a door.',
              'The higher you climb the better the view.',
              'With patience you can even cook a stone.',
              'Don\’t tell me the sky\’s the limit when there\’s footprints on the moon.',
              'If you wanna fly, you got to give up the shit that weighs you down.',
              'I would like to be the air that inhabits you for a moment only. I would like to be that unnoticed and that necessary.',
              'You do not have to be good. You do not have to walk on your knees for a hundred miles through the desert, repenting. You only have to let the soft animal of your body love what it loves.',
              'I want to do with you what spring does with the cherry trees.',
              'Life loves to be taken by the lapel and told: I am with you kid. Let us go.',
              'Courage is not the absence of fear, but rather the judgement that something else is more important than fear.',
              'Always forgive your enemies; nothing annoys them so much.',
              'Though my soul may set in darkness, it will rise in perfect light, I have loved the stars too fondly to be fearful of the night.',
              'All that spirits desire, spirits attain.',
              'At the entrance, my bare feet on the dirt floor, Here, gusts of heat; at my back, white clouds. I stare and stare. It seems I was called for this: To glorify things just because they are.',
              'Who has seen the wind? Neither you nor I but when the trees bow down their heads, the wind is passing by.',
              'The burden of the self is lightened with I laugh at myself.',
              'I know that I shall meet my fate somewhere among the clouds above; those that I fight I do not hate, those that I guard I do not love.',
              ]

def get_input():
    """Welcome to the listening bot. How are you feeling today?"""

    answer = raw_input("...")
    answer = answer.lower()

    return answer


def mishti():
    """Main loop."""
    greeting = "Welcome to the listening bot. How are you feeling today?"
    print greeting


#          

    # While user does not input "bye" or equivalent: 
    while True:
         #  Read raw_input from user
        answer = get_input()
        print "You are feeling ", answer
        sentiment = SentimentIntensityAnalyzer(lexicon_file= 'vader_lexicon.txt')
        sentiment_score = sentiment.polarity_scores(answer)
        if sentiment_score['neg'] > 0:
            print random_quote(inspirational_quotes)
            break
        # The answer was negative
        elif sentiment_score['pos'] > 0:
            print "I am glad you are doing well. Come chat with me any time."
            #Print "How do you feel now?"
            # Print "Bye! Come see me again any time." 

def random_quote(quote_list):
   
    listlen = len(quote_list)
    #random.randint returns a random integer in between the first parameter and last
    random_index = random.randint(0, listlen - 1)
    print quote_list[random_index]
    # We access items in a list by using square brackets and a index. The data type of random_index is integer and that is why we can use it in pull_quote.  

mishti()
