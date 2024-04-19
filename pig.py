import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players.")
    else:
        print("Invalid. Try again.")


while True:
    chosen_max_score = input("Please choose a max score: ")
    if not chosen_max_score.isdigit():
        print("Please choose a whole number!")
        continue
    elif int(chosen_max_score) < 6:
        print("Max score must larger than or equal to 6")
        continue
    else:
        break


max_score = int(chosen_max_score)

player_scores = [0 for num_of_players in range(players)]


while max(player_scores) < max_score:
    for player_index in range(players):
        print(f"\nPlayer number {player_index + 1}'s turn has just started!")
        print(f"Your Total score is: {player_scores[player_index]}\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a '1'! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")
                if current_score >= max_score:
                    break

            print(f"Your score is: {current_score}")

        player_scores[player_index] += current_score
        print(f"Your total score is: {player_scores[player_index]}")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"Player number {winning_idx + 1} "
      f"is the winner with the score of {max_score}")









