#Write your code below this line 👇
def prime_checker(number):
    # is_prime = True
    # for denominator in range(2,number):
    #     if number % denominator == 0:
    #         is_prime = False
    #         break
    # if is_prime:
    #     print("It's a prime number.")
    # else:
    #     print("It's not a prime number.")


    is_prime = True
    for denominator in range(2,number):
        if number % denominator == 0:
            is_prime = False
            print("It's not a prime number.")
            break
    if is_prime:
        print("It's a prime number.")
    




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)