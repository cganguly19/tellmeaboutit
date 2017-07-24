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
        #to do  Use NLTK on raw_input to determine if response is negative or positive
        #If negative : 
        if answer == "sad":
            #Give comforting quote 
            print "Federer just won his eight Wimbeldon at 35. You can do it!"
           
        #If positive:    
        elif answer == "happy":
            #  Give happy quote 
            print "A smile is a curve that sets things straight. Keep smiling."
            break
            #Print "How do you feel now?"
            # Print "Bye! Come see me again any time." 


mishti()
