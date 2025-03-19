"""
#  Overview

- For this challenge, you need to write a function that returns the minimum number of jumps a frog has to make to get to specific target.


#  My Analysis
   First, this a test on time complexity - How long (in compute time) does it your code take during execution? How efficient is your algorithm? 
   While it is possible to use a brute force solution, where you utilise a while loop to check at each iteration whether the frog has covered
   a distance >= Y(Target), the time complexity for this is O(n). 
   
   However, by calculating the distance between the frog's initial position and the target, then determining the total number of jumps 
   it would take the frog to get to the targt - runtime is now a constant O(1) because the dominant operation runs only once.
    
# My Steps:

1. Calculate the total distance (difference between the target and the frog's starting position.)
2. Using an if statement, check whether the modulus of the total distance and the length of the frog's jump is not zero,
   if true, divide the total distance by the frog's jump length, then add one to the steps and return it. (This is because the frog will have 
   to take an extra step to get to a position greater than Y.)
3. If the statement is false, divide the total distance by the frog's jump length and return it. (This is because the frog lands on the target position.)

"""

def solution(X, Y, D):

    total_distance = Y - X

    if (total_distance % D != 0 ):
        steps = total_distance // D + 1

        return steps
    else:
        steps = total_distance // D

        return steps


testcase1 = solution(3, 35, 5)
print(testcase1)


