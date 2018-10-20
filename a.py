"""

Authors:        Gabriel Duarte and Elliot Newman
Class:          CS415 Algorithm Analysis
Assignment:     Project 2
Date:           10/18/2018
Description:    Code Karatsuba's Algorithm and Exponentiation Algorithm
                to show efficiency in run time.

"""


def karatsuba(first_num, second_num, d):
    # Create the arrays for storing digits by 1 digit per index
    fn = []
    sn = []
    n = ''
    n2 = ''
    if (len(first_num) == 1 and len(second_num) == 1):
        mult = int(first_num) * int(second_num)
        return mult


    if (len(first_num) < len(second_num)):
        while (len(first_num) != len(second_num)):
            first_num = '0' + first_num
    if (len(first_num) > len(second_num)):
        while (len(first_num) != len(second_num)):
            second_num = '0' + second_num


    num_of_digits = len(first_num)

    split = (num_of_digits // 2)

    if (num_of_digits % 2 != 0):
        split += 1

    i = 0
    j = num_of_digits//2+num_of_digits-1
    while ( i < num_of_digits):
        if ( j-1 == i and num_of_digits %2 == 1):
            first_num = first_num[:i] + '0' + first_num[i:]
            second_num = second_num[:i] + '0' + second_num[i:]
            fn.append('0')
            sn.append('0')
            i += 1
            num_of_digits += 1

        fn.append(first_num[i])
        sn.append(second_num[i])
        i += 1

    zp = num_of_digits - split
    zp1 = zp * 2

    if (int(first_num) % 2 == 1 and (len(first_num) > 2 or len(second_num) > 2)):
        zp1 -= 2
        zp -= 1
    for i in range(zp1):
        n+='0'
    for i in range(zp):
        n2 += '0'
    a1 = fn[:split]
    b1 = sn[:split]
    a0 = fn[split:]
    b0 = sn[split:]
    i = 0

    c2 = int(karatsuba("".join(a1), "".join(b1), d))
    c0 = karatsuba("".join(a0), "".join(b0), d)
    c1 = karatsuba(str(int("".join(a1)) + int("".join(a0))),str(int("".join(b1)) + int("".join(b0))), d) - (c2 + c0)
    p2 = str(c2) + n
    p1 = str(c1) + n2
    p0 = c0
    c  = int((int(str(c2) + n)) + (int(str(c1) + n2)) + int(c0))
    return c


def Exponentiation(a, n):
    result = a

    for i in range(n - 1):
        result *= a
        print(karatsuba(str(result), str(a)))
        # result *= a
    return result
    #    else
    #       if (n % 2 == 0):
    #          return
    """
    a^n =
    (a^n/2)^2           if n is even and positive,
    (a^(n-1)/2)^2 * a   if n is odd,
    1                   if n = 0.
    """


def main():
    # 5//2 = 2  NOT  3
    x = '0'

    # Loop until the user wants to exit
    while (x != '3'):

        # Ask which Task the user would like to run
        print("\n1: Karatsuba's Algorithm")
        print("2: Exponentiation")
        print("3: Quit\n")
        print("Which option would you like? ")
        x = input()

        # Run Karatsuba's Algorithm
        if (x == '1'):
            # Grab some input from the user
            first_num = str(input("\nPlease enter a number less than or equal to 1000: "))
            second_num = str(input("Please enter another number less than or equal to 1000: "))
            print("\nThe product of", first_num, "and", second_num, "is:", int(int(first_num) * int(second_num)))
            d = len(first_num)
            c = karatsuba(first_num, second_num, d)
            print("Product after karatsuba is: ", c)

        # Run Exponentiation Algorithm
        elif (x == '2'):
            # Grab some input from the user
            a = int(input("\nPlease enter a number less than or equal to 1000 for the constant: "))
            n = int(input("Please enter another number less than or equal to 1000 for the power: "))
            result = Exponentiation(a, n)
            print("Final Value:", result)
        # Exit
        else:
            exit


main()
