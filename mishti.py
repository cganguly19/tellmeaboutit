def get_input():
    """Welcome to the listening bot. How are you feeling today?"""

    answer = raw_input("...")
    answer = answer.lower()

    return answer


def mishti():
    """Main loop."""
    greeting = "Welcome to the listening bot. How are you feeling today?"
    print greeting

#     Print "Welcome to the listening bot. How are you feeling today?"
# While user does not input "bye" or equivalent: 
#     Read raw_input from user
#     Use NLTK on raw_input to determine if response is negative or positive
#     If negative : 
#         Give comforting quote 
#     If positive:
#         Give happy quote    
#     Print "How do you feel now?"
# Print "Bye! Come see me again any time."       

    while True:

        answer = get_input()
        print "You are feeling ", answer

        if answer == "sad":
            print "Federer just won his eight Wimbeldon at 35. You can do it!"
#             if negative : 
# #         Give comforting quote 

        elif answer == "happy":
            print "A smile is a curve that sets things straight. Keep smiling."
            break


mishti()
