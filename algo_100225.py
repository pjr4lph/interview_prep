"""
Remove duplicates from list in place. The sorted list includes numbers in a non-decreasing order.
Order of the numbers should be kept in place.

first thought plan: 
- save the last number in variable
- create one pointer
- iterate up the list, break out when one of the pointers equals the last number
- slice out dups from list
- return input list
"""

def remove_dups(arr):
  i = 0
  while (i < len(arr)-1):
    if arr[i] == arr[i+1]:
      del arr[i]
    else:  
      i+=1
  return arr
  
test_list = [1,2,2,3,4,4,4,5,5]
test_list_2 = [1,2,2,3]
# print('should equal: [1,2,3,4,5]', remove_dups(test_list))

"""
Supposedlyyy better solution:
- create two pointers
- iterate thru list
- if they dont equal
  - switch values

"""

"""
count the frequency of a num in a list. 
ex: Input:  arr[] = [10, 20, 10, 5, 20]
    Output: [[5, 1], [10, 2], [20, 2]]

first thought plan - iterate thru the list use a map which counts or creates a 
new key with values. iterate said map to produce shape of result
"""

def count_freq_list(nums):
  num_count_dict = {}
  # iterate nums
  for num in nums:
    if num_count_dict.get(num, False):
      num_count_dict[num] = num_count_dict.get(num) + 1
    else:
      num_count_dict[num] = 1
  
  # return list(map(lambda kv: list(kv), num_count_dict.items()))
  return [list(kv) for kv in num_count_dict.items()]

count_test = ([1,1,2,3,3,4,4,7], [[1,2],[2,1],[3,2],[4,2],[7,1]])
count_test_2 = ([2,3,3,9], [[2,1],[3,2],[9,1]])

print(count_freq_list(count_test[0]), 'should equal: ', count_test[1])
print(count_freq_list(count_test_2[0]), 'should equal: ', count_test_2[1])

"""
Given an integer array, move all elements that are 0 to the left while maintaining 
the order of other elements in the array. The array has to be modified in-place.


"""