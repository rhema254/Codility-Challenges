# Missing Integer
def solution(A):
    mylist = sorted(A) 

    smallest_number = mylist[0]  
    greatest_number = mylist[-1]  

    new_list = range(smallest_number, greatest_number + 1)

    for x in new_list:
        if x not in mylist:
            if x < 0:
                return 1
            else:
                return x  

    
    return greatest_number + 1

# Test case
test_list = [-1,-3]
smallest = solution(test_list)
print(smallest)  
