# Missing Integer Solution

""" 
#  Overview

- This challenge seeks to find the smallest positive integer that is missing in the given array. 

#  My Approach
  In this challenge, using the provided function, I created 2 test arrays to test out my function, and found the 
  last one after my code failed to pass all 3 checks. Always 'run code' so that you can see the test cases in 
  provided in each of the Checks in the console.


# My Steps:

 1. Sort the input list into Ascending Order.
 2. Get the first and last indexes in the List in order to create a range.
 3. Create a new list using the range provided by the First and Last indexes.
 4. Use a for loop to iterate over the elements of the new_list.
 5. Inside the for loop, use an if statement to check for missing element(s) in 'mylist'(The original list). 
 6. [A caveat] Add an if statement to handle cases where elements in the test case are -ve and simply assume 1 as the missing element
     or else simply return the value of x, which will be the leftmost and smallest value which does not exist in

"""

def solution(A): 
    mylist = sorted(A) 

    smallest_number = mylist[0]  
    greatest_number = mylist[-1]  

    new_list = range(smallest_number, greatest_number + 1)

    for x in new_list:     # Loop through each element in the new list. 
        if x not in mylist:  # Check whether the element in the iteration is in both lists.
            if x < 0:           
                return 1 #For -ve number use-cases.
            else:
                return x  # For +ve non-zero number use-cases. 

    
    return greatest_number + 1

# Test case
#test_list = [1,2,3]
#test_list = [1, 3, 6, 4, 1, 2]
test_list = [-1,-3]
smallest = solution(test_list)
print(smallest)  
