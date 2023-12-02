from art import name_art, name_art2, with_player, with_computer, game_art_base
from replit import clear
import random

print(name_art)

positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("""Game Rules:
Each available position in the game is attached to a number, between 1 to 9.
""")
winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
available_positions = positions
game_art = game_art_base
player1_score = 0
player2_score = 0
game_on = True
while game_on:
    user_choice = int(input("""Please select to continue\n1. 2 Player Game\n2. Play with computer(not available 
    currently) \nEnter 1 or 2: """))

    if user_choice == 1:
        clear()
        print(with_player)
        turn = [0, 1]
        start_turn = random.choice(turn)
        print(game_art)
        player1_hand = []
        player2_hand = []
        win_flag = False
        winner = 3
        inner_loop = True
        while inner_loop and len(available_positions) > 0:
            if win_flag:
                inner_loop = False
            else:
                if start_turn == 0:
                    element_check = True
                    while element_check:
                        player1_choice = int(input("Player 1's turn: "))
                        if player1_choice not in available_positions:
                            print('This position is not available. Please try again.')
                        else:
                            element_check = False
                    player1_hand.append(player1_choice)
                    available_positions.remove(player1_choice)
                    game_art = game_art.replace(str(player1_choice), 'X')
                    print(game_art)
                    # print(player1_hand, len(player1_hand))
                    start_turn = 1
                else:
                    element_check = True
                    while element_check:
                        player2_choice = int(input("Player 2's turn: "))
                        if player2_choice not in available_positions:
                            print('This position is not available. Please try again.')
                        else:
                            element_check = False
                    player2_hand.append(player2_choice)
                    available_positions.remove(player2_choice)
                    game_art = game_art.replace(str(player2_choice), 'O')
                    print(game_art)
                    # print(player2_hand, len(player2_hand))
                    start_turn = 0

            if len(player1_hand) >= 3:
                for combination in winning_combinations:
                    count = 0
                    for i in combination:
                        if i in player1_hand:
                            count += 1
                    if count == 3:
                        win_flag = True
                        winner = 1
            if len(player2_hand) >= 3:
                for combination in winning_combinations:
                    count = 0
                    for i in combination:
                        if i in player2_hand:
                            count += 1
                    if count == 3:
                        win_flag = True
                        winner = 2

        if len(available_positions) == 0:
            print("It's a Draw!")
        if winner == 1:
            player1_score += 1
            print('Player 1 wins.')
        if winner == 2:
            player2_score += 1
            print('Player 2 wins.')
        print(f"Player 1's score: {player1_score}\nPlayer 2's score: {player2_score}")

        ask_again_loop = True
        while ask_again_loop:
            play_again = input('\n\nPlay again. Type Y/Yes or N/No: ').lower()
            if play_again == 'y' or play_again == 'yes':
                game_on = True
                ask_again_loop = False
                game_art = game_art_base
                available_positions.clear()
                available_positions.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
                # print(available_positions)
            elif play_again == 'n' or play_again == 'no':
                game_on = False
                ask_again_loop = False
                clear()
                print(f"FINAL SCORE:\nPlayer 1 : {player1_score}\nPlayer 2 : {player2_score}")
            else:
                print("Please select correct option.")


    elif user_choice == 2:
        clear()
        print(with_computer)

    else:
        print('Wrong choice. Please Try Again.')