import random, copy, time
card_Deck = {'A': '1', 'A': '11', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
             '7': '7', '8': '8', '9': '9', '10': '10', 'J': '10',
             'Q': '10', 'K': '10'}
print("Welcome to BLACKJACK!\n\n")
time.sleep(1.5)
print("Attempt to beat the dealer by getting as close to 21 as possible, without going over.\n")
time.sleep(3)

#players turn
loop_One = True
loop_Two = True
loop_Three = True
while loop_One:
    player_Cards = []
    player_Score = []
    dealer_Cards = []
    dealer_Score = []
    did_Player_Bust = False
    did_Dealer_Bust = False
    player_Cards.append(random.choice(list(card_Deck)))
    player_Cards.append(random.choice(list(card_Deck)))
    dealer_Cards.append(random.choice(list(card_Deck)))
    dealer_Cards.append(random.choice(list(card_Deck)))
    print("You are dealt two cards face down, that only you can see.\nThe dealer is also dealt two cards.\nOne of the dealer's cards was dealt face up.\n\n")
    time.sleep(3)
    while loop_Two:
        print('The cards you have are: ' + str(player_Cards) + '.')
        time.sleep(3)
        player_Score.clear()
        for cards in player_Cards:
            player_Score.append(int(card_Deck.get(cards, 0)))
        for x in range(0, len(player_Score)):
            player_Score[x] = int(player_Score[x])
        player_Score_Sum = sum(player_Score)
        print("Your card's total points are: " + str(player_Score_Sum) + ".\n")
        time.sleep(3)
        print("The dealer has a ['" + dealer_Cards[0] + "'] showing.")
        while loop_Three:
            if player_Cards == ['A', 'K'] or player_Cards == ['A', 'Q'] or player_Cards == ['A', 'J'] or player_Cards == ['A', '10'] or player_Cards == ['K', 'A'] or player_Cards == ['Q', 'A'] or player_Cards == ['J', 'A'] or player_Cards == ['10', 'A']:
                time.sleep(2)
                loop_One = False
                loop_Two = False
                loop_Three = False
            if player_Score_Sum >= 22:
                print('Bust!')
                did_Player_Bust = True
                time.sleep(2)
                print('\nThe dealer reveals his cards.\n')
                time.sleep(2)
                loop_One = False
                loop_Two = False
                loop_Three = False
            if player_Score == 21:
                time.sleep(2)
                print('\nThe dealer reveals his cards.\n')
                time.sleep(2)
                loop_One = False
                loop_Two = False
                loop_Three = False
            if player_Score_Sum <= 21:
                player_Choice = input('Do you want another card?\n')
                if player_Choice == 'y':
                    player_Cards.append(random.choice(list(card_Deck)))
                    print('\nYou hit!\n')
                    print('The cards you have are: ' + str(player_Cards) + '.')
                    time.sleep(3)
                    player_Score.clear()
                    for cards in player_Cards:
                        player_Score.append(int(card_Deck.get(cards, 0)))
                    for x in range(0, len(player_Score)):
                        player_Score[x] = int(player_Score[x])
                    player_Score_Sum = sum(player_Score)
                    print("Your card's total points are: " + str(player_Score_Sum) + ".\n")
                    continue
                elif player_Choice == 'n':
                    time.sleep(2)
                    print('\nThe dealer reveals his cards.\n')
                    time.sleep(2)
                    loop_One = False
                    loop_Two = False
                    loop_Three = False
                else:
                    print("Enter 'y' for yes or 'n' for no.")
                    continue
    #dealers turn
    print('The cards the dealer has are: ' + str(dealer_Cards))
    dealer_Score.clear()
    for cards in dealer_Cards:
        dealer_Score.append(int(card_Deck.get(cards, 0)))
    for x in range(0, len(dealer_Score)):
        dealer_Score[x] = int(dealer_Score[x])
    dealer_Score_Sum = sum(dealer_Score)
    time.sleep(1)
    print("The dealer's card's points are: " + str(dealer_Score_Sum))

    #dealers turn (hit or stay)
    while True:
        if did_Player_Bust == True:
            break
        if int(dealer_Score_Sum) < 17:
            dealer_Cards.append(random.choice(list(card_Deck)))
            time.sleep(2)
            print('The dealer hits!\n')
            print('The cards the dealer has are: ' + str(dealer_Cards))
            dealer_Score.clear()
            for cards in dealer_Cards:
                dealer_Score.append(int(card_Deck.get(cards, 0)))
            for x in range(0, len(dealer_Score)):
                dealer_Score[x] = int(dealer_Score[x])
            dealer_Score_Sum = sum(dealer_Score)
            print("The dealer's card's points are: " + str(dealer_Score_Sum))
            continue
        if int(dealer_Score_Sum) > 21:
            did_Dealer_Bust = True
            break
        else:
            break

    #results
    time.sleep(3)
    if player_Cards == ['A', 'K'] or player_Cards == ['A', 'Q'] or player_Cards == ['A', 'J'] or player_Cards == ['A', '10'] or player_Cards == ['K', 'A'] or player_Cards == ['Q', 'A'] or player_Cards == ['J', 'A'] or player_Cards == ['10', 'A']:
        print('Blackjack!\nYou won!')
    if did_Player_Bust == True:
        print('You lost!')
    if did_Player_Bust == False and did_Dealer_Bust == True:
        print('The dealer folded!\nYou won!')
    else:
        if player_Score_Sum < dealer_Score_Sum:
            print('You lost!')
        if player_Score_Sum > dealer_Score_Sum and did_Player_Bust == False:
            print('You won!')
        if player_Score_Sum == dealer_Score_Sum:
            print("It's a push!")

    #replay
    time.sleep(3)
    replay = input('\nDo you want to play again?\n')
    if replay == 'y':
        player_Cards.clear()
        dealer_Cards.clear()
        player_Score.clear()
        dealer_Score.clear()
        player_Score_Sum = 0
        dealer_Score_Sum = 0
        loop_One = True
        loop_Two = True
        loop_Three = True
        print('\n\n\n')
        continue
    if replay == 'n':
        break
