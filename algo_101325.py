"""
remove duplicates after second dup from array in place
- input: array of integers
- output: length of final array
ex: [1,1,1,2,2,3] --> [1,1,2,2,3]
plan: - update - iterate thru list and compare i-2 to see if values match, if match delete current item
"""

def remove_dups(nums):

  i = 2
  length_counter = len(nums)
  while (length_counter > 1):
    if nums[i] == nums[i-2]:
      del nums[i]
      length_counter -= 1
      i -= 1    
    i += 1
    length_counter -= 1
    
  return nums

print('test: ',  remove_dups([1,1,1,2,2,3]))
print('test 2: ',  remove_dups([1,1,1,2,2,2,2,3,3,3]))

    
