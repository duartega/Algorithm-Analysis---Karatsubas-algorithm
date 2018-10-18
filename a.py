"""

Authors:        Gabriel Duarte and Elliot Newman
Class:          CS415 Algorithm Analysis
Assignment:     Project 2
Date:           10/18/2018
Description:    Code Karatsuba's Algorithm and Exponentiation Algorithm
                to show efficiency in run time.

"""


def karatsuba(first_num, second_num):
    # Create the arrays for storing digits by 1 digit per index
    fn = []
    sn = []

    # Make sure that the numbers are 1 digit
    if (int(first_num) < 10 and int(second_num) < 10):
        mult = int(first_num) * int(second_num)
        return mult

    # Checks to see if the numbers have the same length for
    # easier multiplication. Pad with zero on left if not the same length
    if (len(first_num) < len(second_num)):
        while (len(first_num) != len(second_num)):
            first_num = '0' + first_num
    elif (len(first_num) > len(second_num)):
        while (len(first_num) != len(second_num)):
            second_num = '0' + second_num

    # Set the number of digits to the length of
    # the string provided
    num_of_digits = len(first_num)

    # Append each number as a single digit to
    # their respective arrays
    for i in range(num_of_digits):
        fn.append(int(first_num[i]))
        sn.append(int(second_num[i]))

    # Get the number of first half of elements for a1 and b1
    split = (len(fn)//2)

    # If there are only 3 elements, 3//2 = 1
    # but you need at least the first 2 in the array
    if (split % 2 == 1):
        split += 1

    # Python syntax to get the indexes from
    # [0:split] and [split:] Ex: split = 2,
    # [0:2] would get the first two elements
    if (num_of_digits == 2):
        a1 = fn[:split]
        b1 = sn[:split]
    else:
        a1 = fn[:split]
        b1 = sn[:split]
        a0 = fn[split:]
        b0 = sn[split:]

    # Calculate a two digit number times another two digit number
    if (num_of_digits == 2):
        c2 = karatsuba(str(a1[0]),str(b1[0]))
        c0 = karatsuba(str(a1[1]),str(b1[1]))
        c1 = karatsuba(str(a1[0] + a1[1]) , str(b1[0] + b1[1])) - (c2 + c0)
        c  = (int(str(c2) +'00')) + (int(str(c1) +'0')) + c0
        return c

    # Calculate a three digit number times another three digit number Ex: 123 * 123
    if (num_of_digits == 3):
        c2 = karatsuba((str(a1[0])+str(a1[1])),(str(b1[0])+str(b1[1]))) # Ex: 12 * 12
        c0 = a0[0] * b0[0] # We know this will always be a single digit since the length is odd. # Ex: 3 * 3
        c1 = karatsuba(str(int(str(a1[0]) + str(a1[1]))+ int(str(a0[0]))), str(int(str(b1[0]) + str(b1[1]))+ int(str(b0[0]))) ) - (c2 + c0)
        c  = (int(str(c2) +'00')) + (int(str(c1) +'0')) + c0
        return c

    # Calculate a four digit number times another four digit number Ex: 2299 * 4412
    if (num_of_digits == 4):
        c2 = karatsuba((str(a1[0])+str(a1[1])),(str(b1[0])+str(b1[1]))) # xx * xx Ex: 22 * 44
        c0 = karatsuba((str(a0[0])+str(a0[1])),(str(b0[0])+str(b0[1]))) # xx * xx Ex: 99 * 12
        c1 = karatsuba(str(int(str(a1[0]) + str(a1[1]))+ int(str(a0[0])+str(a0[1]))), str(int(str(b1[0]) + str(b1[1]))+ int(str(b0[0]) + str(b0[1]))) ) - (c2 + c0)
        c  = int(str(c2) + '0000') + int(str(c1) + '00') + int(c0)
        return c

def main():
    # 5//2 = 2  NOT  3
    x = '0'

    # Loop until the user wants to exit
    while(x != '3'):

        # Grab some input from the user
        first_num = (input("\nPlease enter a number less than or equal to 1000: "))
        second_num = (input("Please enter another number less than or equal to 1000: "))

        # Ask which Task the user would like to run
        print("\n1: Karatsuba's Algorithm")
        print("2: Exponentiation")
        print("3: Quit\n")
        print("Which option would you like? ")
        x = input()

        # Run Karatsuba's Algorithm
        if (x == '1'):
            print("\nThe product of", first_num, "and", second_num, "is:", int(int(first_num)*int(second_num)))
            c = karatsuba(first_num, second_num)
            print("Product after karatsuba is: ", c )

        # Run Exponentiation Algorithm
        elif(x == '2'):
            print("Not yet implemented")

        # Exit
        else:
            exit

main()