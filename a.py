


def karatsuba(first_num, second_num):
    fn = []
    sn = []
    c  = 0
    c0 = 0
    c1 = 0
    c2 = 0

    # Make sure that the numbers are 1 digit
    if (int(first_num) < 10 and int(second_num) < 10):
        mult = int(first_num) * int(second_num)
        print("No need for karatsub's algorithm... Product is:", mult)
        return 0

    # Checks to see if the numbers have the same length for
    # easier multiplication
    if (len(first_num) < len(second_num)):
        while (len(first_num) != len(second_num)):
            first_num = '0' + first_num
    elif (len(first_num) > len(second_num)):
        while (len(first_num) != len(second_num)):
            second_num = '0' + second_num        
    
    
    ## want to check if we should convert 123 * 123 to 0123 * 0123


    # Set the number of digits to the length of
    # the string provided
    num_of_digits = len(first_num)

    
    # Append each number as a single digit to
    # their respective arrays
    for i in range(num_of_digits):
        fn.append(int(first_num[i]))
        sn.append(int(second_num[i]))

    # Get the first half for a1 and b1
    split = (len(fn)//2)

    # If there are only 3 elements, 3//2 = 1
    # but you need at least the first 2 in the array
    if (split % 2 == 1):
        split += 1
    
    # Python syntax to get the indexes from
    # [0:split] and [split:end]
    if (num_of_digits == 2):
        a1 = fn[:split]
        b1 = sn[:split]
        #print("a1:", a1)
        #print("b1:", b1)
    else:
        a1 = fn[:split]
        b1 = sn[:split]
        a0 = fn[split:]
        b0 = sn[split:]
        #print("a1:", a1)
        #print("b1:", b1)
        #print("a0:", a0)
        #print("b0:", b0)

        
    if (num_of_digits == 2):
        ret = calculate2(a1,b1)
        print("Product after karatsuba is: ", ret)
        return 0
    if (num_of_digits == 3):
        c2 = calculate2(a1,b1)
        c0 = a0[0] * b0[0]
        c1 = (int(str(a1[0]) + str(a1[1])) + a0[0]) * (int(str(b1[0]) + str(b1[1])) + b0[0]) - (c2 + c0)
        c  = (c2 * 10**2) + (c1 * 10) + c0
        print("Product after karatsuba is: ", c )
        return 0
    if (num_of_digits == 4):
        ret = calculate2(a1,b1)
        ret1 = calculate2(a0,b0)
        print("4ret",ret)
        print("4ret1:",ret1)
        return 0
    print(*fn)
    print(*sn)

def calculate2(n1, n2):
    c2 = n1[0]*n2[0]
    c0 = n1[1]*n2[1]
    c1 = (n1[0] + n1[1]) * (n2[0] + n2[1]) - (c2 + c0)
    c  = (c2 * 10**2) + (c1 * 10) + c0
    #print("Product after karatsuba is: ", c )
    return c

def main():
    #print(5//2) = 2  NOT  3
    x = '0'
    while(x != '3'):
        first_num = (input("\nPlease enter a number less than or equal to 1000: "))
        second_num = (input("Please enter another number less than or equal to 1000: "))
        
        print("\n1: Karatsuba's Algorithm")
        print("2: Exponentiation")
        print("3: Quit\n")
        print("Which option would you like? ")
        x = input()
        if (x == '1'):
            print("\nThe product of", first_num, "and", second_num, "is:", int(int(first_num)*int(second_num)))
            karatsuba(first_num, second_num)
        elif(x == '2'):
            print("Not yet implemented")
        else:
            exit

main()