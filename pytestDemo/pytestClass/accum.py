import random


def check_score(score):
    if score == 0:
        print("exceed the attempts")
        return True


def sample():
    user_name = input("please enter ur name \n")
    print("hi {}, welcome to the number guessing game".format(user_name))
    ready = input("shall we start the game (yes/no)\n")

    sys_gen_num = random.randrange(1, 10)
    score = 5
    while ready == "yes":
        user_guess = int(input("please guess the number between 1 and 10\n"))
        if user_guess <= 0 or user_guess >= 11:
            user_guess = int(input("please enter the number ranging between 1 to 10\n"))

        if user_guess == sys_gen_num:
            print("Great, u guessed the number correct")
            print("ur score is", score)
            break

        elif user_guess > sys_gen_num:
            print("guess lesser number")
            score -= 1

            bol = check_score(score)
            if bol:
                break

        elif user_guess < sys_gen_num:
            print("guess greater number")
            score -= 1
            bol = check_score(score)
            if bol:
                break


sample()
