print("\nQ1a\n")


# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def fone(num):
    listed = []
    for i in range(1, num + 1):
        if num % i == 0:
            listed.append(i)
    return listed


print(fone(12))

print("\nQ1b\n")


# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def ftwo(num1=int, num2=int):
    listedone, listedtwo = fone(num1), fone(num2)
    print(listedone, listedtwo)
    if listedone in listedtwo or listedtwo in listedone:
        return True
    else:
        return False


print(ftwo(24, 4))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", " "]


# A2a:
def charindex(letter):
    # letter = input("choose a letter ")
    if letter in alphabet:
        return print(alphabet.index(letter))

    else:
        print("invalid entry")


charindex('j')

print("\nQ2b\n")


# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def nameId(name=str):
    id = []
    for char in name.lower():
        id.append(alphabet.index(char))
    return ''.join(str(i) for i in id)


katid = nameId("Kat")
print(katid)

print("\nQ2c\n")


# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and
# 1+1+4+1 = 7 so
# 1141 - 7 = 1134

# A2c:
def password():
    name = katid
    namesum = 0
    for num in name:
        namesum += int(num)
    return int(name) - namesum


print(password())

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")


# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
#
def prime_check():
    number = input("Choose a number to use in the prime checker ")
    prime_status = False
    for a in range(2, number):
        if number == 1:
            prime_status = False
            return prime_status
        elif number > 1:
            for num in range(2, number):
                if number % num == 0:
                    prime_status = False
                    break
            if prime_status:
                return prime_status
            else:
                return prime_status


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b: #NOT WORKING
#
def is_prime():
    not_integer = True
    number = 0
    while not_integer:
        try:
            print('what prime number would you like to check:')
            number = int(input())
            if type(number) == int:
                not_integer = False
        except ValueError:
            print('enter a integer/number')

    prime = True
    if number == 1:
        prime = False
        return prime
    elif number > 1:
        for num in range(2, number):
            if number % num == 0:
                prime = False
                break
        if prime:
            return prime
        else:
            return prime


print(is_prime())



