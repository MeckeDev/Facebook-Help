# creating the Function to pick the Winner
def who_is_winner(votes):

    # getting a List of unique Names of Participants
    participants = set(votes)

    # empty Dictionary to save the Amount of Votes per Participant
    vote_list = {}

    # counting all votes for each Participant
    for participant in participants:

        # List comprehension to count every occurence of the Name
        amount = [i for i in votes if i == participant]

        # saving the amount of Votes in the Dictionary
        vote_list[participant] = len(amount)

    # sorting the Dictionary by the Amount of Votes
    # to get the most Voted Participants to the beginning
    vote_list = sorted(vote_list.items())

    # winning Amount is the Number the Paticipant with the most Votes reached
    winning_amount = vote_list[0][1]

    # creating an empty List in Case multiple People got a Draw
    winners = []

    # checking the sorted Dictionary if more than 1 Participant has won
    for i in vote_list:
        if i[1] == winning_amount:
            winners.append(i[0])


    # This is the Message we print for a single Winner
    if len(winners) == 1:
        print(f"{winners[0]} has won with {winning_amount} Votes.")
        
            #   if you only want the Name of the Winner just do it like here
            #   print(winners[0]) 
    
    else:

        # if we have more than one Winner i want to produce a correct Response
        # if you just want to return a List of Winners, skip this part until you see a Line like below
        ### ###################################################################################### ###
        win_notification = "The Winners are "

        # this is the Amount of different Winners, if the got the same Amount of Votes
        winners_ = len(winners)

        # this a Loop where we get all Winners except the last one
        # to add them to the Notification seperated with a Comma
        for i in range(0, winners_ - 1):
            win_notification += f"{winners[i]}, "

        # now we remove the last Comme added by the Loop
        win_notification = win_notification[:-2]

        # and adding the last Winner with an "and" to get a Notification like
        # The Winners are Amy, Lisa and Kim 
        # instead of 
        # the Winners are Amy, Lisa, Kim 

        # after that we also add the Amount of Votes they got 
        win_notification += f" and {winners[winners_ -1]} they got {winning_amount} Votes."

        # printing the Notification we have created
        print(win_notification)

        ### ###################################################################################### ###

            # we could also just print the Winners as a List like here
            #print(winners)

# Feeding the Function with Votes
who_is_winner(["Amy", "Amy", "Lisa", "Amy", "Amy"])

# another Example
who_is_winner(["Amy","Amy", "Lisa","Lisa","Lisa","Amy", "Kim", "Kim", "Kim"])