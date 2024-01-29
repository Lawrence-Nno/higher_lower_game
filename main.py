import random
from game_data import data
from art import logo, vs


def game_on():
    print(logo)
    score = 0
    correct = True
    obj1 = random.choice(data)
    obj2 = random.choice(data)
    while correct:
        print(f"Compare A: {obj1['name']}\na {obj1['description']} from {obj1['country']}")
        print(vs)
        print(f"Against B: {obj2['name']}\na {obj2['description']} from {obj2['country']}")

        ans = input("Who has more followers? Type 'A' or 'B': ")
        if ans.lower() == 'a' and obj1['follower_count'] >= obj2['follower_count']:
            score += 1
            print(f"You are correct. Current score is {score}")
            print()
        elif ans.lower() == 'b' and obj2['follower_count'] >= obj1['follower_count']:
            score += 1
            print(f"You are correct. Current score is {score}")
            print()
        else:
            print(f"You are wrong. Your total score is {score}")
            print()
            continue_game = input("Do you wish to play again? Type 'yes' or 'no'\n")
            if continue_game.lower() == 'yes':
                game_on()
            else:
                break
            return score

        obj1 = obj2
        obj2 = random.choice(data)


if __name__ == '__main__':
    game_on()

