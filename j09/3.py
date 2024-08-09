def prime(a) :
    if a == 2 or a == 3 or a == 5 or a == 7 and a % 2 != 0 and a % 3 != 0 and a % 5 != 0 and a % 7 != 0 :
        print("your number is prime")
    elif a % 2 != 0 and a % 3 != 0 and a % 5 != 0 and a % 7 != 0 :
        print("your number is prime")
    else :
        print("your number is not prime")


prime(int(input("enter your number : ")))