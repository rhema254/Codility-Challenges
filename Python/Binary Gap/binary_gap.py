# Binary Gap Exercise

""" 
#  Overview

- This challenge seeks to find the largest number of 0s between the two 1s in the binary representation of a given input integer. 

#  My Approach
  In this challenge, using the provided function, I created 1 test array to test out my function, and found the 
  other after failed 3 checks. Always 'run code' so that you can see the test cases in  provided in each of the
  Checks in the console.


# My Steps:

 1. Convert the input into binary using the binary function bin() and remove the first two characters that will be added at the beginning. Store it in the same list
 2. Define my counters. count and max_count and set them to 0.
 3. Use a for loop to iterate through each digit of the binary number.
 4. Use a if statement to check whether a digit is 0, if true, increment the count by 1. This will count all the consecutive zeros. It is important to 
    increment the count by 1, so that we get the maximum number of consecutive 0s, which implies, they are between 1s.
 5. Add an else if statement to check whether the digit is 1 and if true, assign the maximum value of count to max_count and then reset count to 0. 
    This ensures that you have the largest value of count i.e, the greatest number of consecutive zeros between two 1s.
 
"""


def solution(N):    
    N = bin(N)[2:]
    
    count = 0
    max_count = 0

    for x in N:
        if int(x) == 0:
            count += 1
        elif int(x) == 1:
            max_count = max(count, max_count)
            count= 0

    return max_count 

# Test Cases
# testNumber = 9
# testNumber = 111
testNumber = 529

testCase = solution(testNumber)
print(testCase)
