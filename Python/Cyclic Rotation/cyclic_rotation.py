# Cyclic Rotation Exercise

""" 
#  Overview

- This challenge requires you to write a function that returns an array rotated K times to the right. 

#  My Approach
  In this challenge, using the provided function, I used arrays present in the question details to test out my function.
  If you're running your code in the codility environment, always 'run code' first so that you can see the test cases
  provided in each of the Checks in the console. Also, look for test arrays present in the question description.


# My Steps:

 1. Create a duplicate of the given input list.
 2. Define my counters. count and max_count and set them to 0.
 3. Use a for loop to iterate through each digit of the binary number.
 4. Use a if statement to check whether a digit is 0, if true, increment the count by 1. This will count all the consecutive zeros. It is important to 
    increment the count by 1, so that we get the maximum number of consecutive 0s, which implies, they are between 1s.
 5. Add an else if statement to check whether the digit is 1 and if true, assign the maximum value of count to max_count and then reset count to 0. 
    This ensures that you have the largest value of count i.e, the greatest number of consecutive zeros between two 1s.
 
"""

def solution(A, k):

    new_list = A.copy()
    length = len(A)

    for x in range(0, length):
        new_list[(x+k)%length] = A[x]
    
    return new_list

#test cases
# A = [3, 8, 9, 7, 6]
# k = 3
# A = [0, 0, 0]
# k = 1
A = [1, 2, 3, 4]
k = 4

testcase = solution(A, k)
print(testcase)