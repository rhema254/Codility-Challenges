def solution(A):
   myArray = list(A)
   myArray.sort()

   count = myArray[0]

   for x in myArray:
    if count == x:
        count = count + 1
    else:
        return count
        


testcase1 = [2,1,3,5]
print(solution(testcase1))