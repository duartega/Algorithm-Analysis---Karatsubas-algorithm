# Group Members:
Gabriel Duarte and Elliot Newman

## Run The Code
type in 'python a.py'<br />
You will enter two numbers less than or equal to 1000.<br />
You will then be able to choose which task you would like to run.<br />

1: Karatsuba's Algorithm<br />
2: Exponentiation<br />
3: Quit<br />

Which option would you like?<br />

If you select task 1, enter two numbers, in this case 1234 and 5678, you will get:<br />

The product of 1234 and 5678 is: 7006652<br />
Product after karatsuba is:  7006652<br />
 
The first line is using the built in * operator to verify that our answer is correct when we run Karatsubas algorithm.<br />

If you select task 2, enter two numbers, this case 2 and 25, you will get:<br />

Built in power function: 33554432<br />
Final Value: 33554432<br />
Time taken: 0.0002601146697998047<br />
These match!<br />

The first line is using the built in pow(a,n) operator to verify that our answer is correct when we run Exponentiation and Karatsubas algorithm on the numbers.<br />

The second line is when we use our created Exponentiation function.<br />

I then output the time that it takes the algorithm to compute these values.<br />

I lastly ouput "These match" if the answer is correct. I do this because you may have a really long number and it may be difficult to compare the answers.<br />