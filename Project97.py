import random
number = random.randrange(1,9,1)
print(" Welcome to the Number guessing game ")
print(" Guess a number between 1 and 9, You will get 5 chances to choose the right option")
i1=int(input(" Enter Your first guess : "))
if i1==number:
    print(" Congratulations your First guess was right")
elif i1>number:
    print("  Your guess was too high: Guess a number lower than ", str(i1))
    i2=int(input(" Enter Your second guess : "))
    if i2==number:
        print(" Congratulations your second guess was right")
    elif i2>number:
        print("  Your guess was too high: Guess a number lower than ", str(i2))
        i3=int(input(" Enter Your third guess : "))
        if i3==number:
            print(" Congratulations your third guess was right")
        elif i3>number:
            print("  Your guess was too high: Guess a number lower than ", str(i3))
            i4=int(input(" Enter Your fourth guess : "))
            if i4==number:
                print(" Congratulations your fourth guess was right")
            elif i4>number:
                print("  Your guess was too high: Guess a number lower than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
            elif i4<number:
                print("  Your guess was too low: Guess a number higher than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
        elif i3<number:
            print("  Your guess was too low: Guess a number higher than ", str(i3))
            i4=int(input(" Enter Your fourth guess : "))
            if i4==number:
                print(" Congratulations your fourth guess was right")
            elif i4>number:
                print("  Your guess was too high: Guess a number lower than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
            elif i4<number:
                print("  Your guess was too low: Guess a number higher than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
    elif i2<number:
        print("  Your guess was too low: Guess a number higher than ", str(i2))
        i3=int(input(" Enter Your third guess : "))
        if i3==number:
            print(" Congratulations your third guess was right")
        elif i3>number:
            print("  Your guess was too high: Guess a number lower than ", str(i3))
            i4=int(input(" Enter Your fourth guess : "))
            if i4==number:
                print(" Congratulations your fourth guess was right")
            elif i4>number:
                print("  Your guess was too high: Guess a number lower than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
            elif i4<number:
                print("  Your guess was too low: Guess a number higher than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
        elif i3<number:
            print("  Your guess was too low: Guess a number higher than ", str(i3))
            i4=int(input(" Enter Your fourth guess : "))
            if i4==number:
                print(" Congratulations your fourth guess was right")
            elif i4>number:
                print("  Your guess was too high: Guess a number lower than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
            elif i4<number:
                print("  Your guess was too low: Guess a number higher than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
elif i1<number:
    print("  Your guess was too low: Guess a number higher than ", str(i1))
    i2=int(input(" Enter Your second guess : "))
    if i2==number:
        print(" Congratulations your second guess was right")
    elif i2>number:
        print("  Your guess was too high: Guess a number lower than ", str(i2))
        i3=int(input(" Enter Your third guess : "))
        if i3==number:
            print(" Congratulations your third guess was right")
        elif i3>number:
            print("  Your guess was too high: Guess a number lower than ", str(i3))
            i4=int(input(" Enter Your fourth guess : "))
            if i4==number:
                print(" Congratulations your fourth guess was right")
            elif i4>number:
                print("  Your guess was too high: Guess a number lower than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
            elif i4<number:
                print("  Your guess was too low: Guess a number higher than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
        elif i3<number:
            print("  Your guess was too low: Guess a number higher than ", str(i3))
            i4=int(input(" Enter Your fourth guess : "))
            if i4==number:
                print(" Congratulations your fourth guess was right")
            elif i4>number:
                print("  Your guess was too high: Guess a number lower than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
            elif i4<number:
                print("  Your guess was too low: Guess a number higher than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
    elif i2<number:
        print("  Your guess was too low: Guess a number higher than ", str(i2))
        i3=int(input(" Enter Your third guess : "))
        if i3==number:
            print(" Congratulations your third guess was right")
        elif i3>number:
            print("  Your guess was too high: Guess a number lower than ", str(i3))
            i4=int(input(" Enter Your fourth guess : "))
            if i4==number:
                print(" Congratulations your fourth guess was right")
            elif i4>number:
                print("  Your guess was too high: Guess a number lower than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
            elif i4<number:
                print("  Your guess was too low: Guess a number higher than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
        elif i3<number:
            print("  Your guess was too low: Guess a number higher than ", str(i3))
            i4=int(input(" Enter Your fourth guess : "))
            if i4==number:
                print(" Congratulations your fourth guess was right")
            elif i4>number:
                print("  Your guess was too high: Guess a number lower than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
            elif i4<number:
                print("  Your guess was too low: Guess a number higher than ", str(i4))
                i5=int(input(" Enter Your fifth guess : "))
                if i5==number:
                    print(" Congratulations your fifth guess was right")
                elif i5>number:
                    print("  Your guess was too high: Your out of guesses and you lose. The number was ", str(number))
                elif i5<number:
                    print("  Your guess was too low: Your out of guesses and you lose. The number was ", str(number))
            
        