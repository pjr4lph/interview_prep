# create function which takes in a number as an array of the 
# individual numbers and add one to that number
"""
example: [1,2,3] --> [1,2,4]
example: [9,9,9] --> [1,0,0,0]

starttime: 1:30pm 
endtime: 

plan of action: 
- iterate backwards from the array 
- check if the number is less than 9
- if so set value to 0
- if less than 9 add 1 and return list
"""

def plus_one(digits):
  for i in range(len(digits)-1, -1, -1):
    if digits[i] < 9:
      digits[i] += 1
      return digits
    digits[i] = 0
    
  return [1] + digits
  

# print(plus_one([1,3,9,9]),'--> [1,4,0,0]')

def pali(string):
  left = 0
  right = len(string) - 1
  while (left < right):
    if string[left] != string[right]:
      return False
    left += 1
    right -= 1

  return True

print(pali('racecar'), '--> True')
print(pali('asdf'), '--> False')