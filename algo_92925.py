"""
Given two sorted arrays arr1[] of size n and arr2[] of size m. Merge these two arrays.
After the merge, the first n smallest elements of the combined sorted array should be 
stored in arr1[], and the remaining m largest elements should be stored in arr2[]. 
After the merging process, both arr1[] and arr2[] must remain sorted in non-decreasing order.

Input: arr1[] = [1, 3, 4, 5], arr2[] = [2, 4, 6, 8] 
Output: arr1[] = [1, 2, 3, 4], arr2[] = [4 5, 6, 8] 
Explanation: Combined sorted array = [1, 2, 3, 4, 4, 5, 6, 8], 
array arr1[] contains smallest 4 elements: 1, 2, 3, 4, and 
array arr2[] contains the remaining 4 elements: 4, 5, 6, 8.
"""

"""
plan: merge the two sorted arrays and reassign smaller half into array 1 and large half into array 2

assumptions: 
- arrays are the same length
- array items are 
- arrays are actually sorted in increasing order

code plan: 
- iterate both arrays with two pointers
- compare each number, 
- if less, push num to merged arr
- increase that pointer

- find middle value
- reassign arrays
"""

def merge_sorted_arrays(arr1, arr2):
  merged_arr = []
  i = 0
  k = 0
  arr1_len = len(arr1)-1
  arr2_len = len(arr2)-1
  # iterate arrays
  while (i <= arr1_len and k <= arr2_len):
    if arr1[i] < arr2[k]:
      merged_arr.append(arr1[i])
      i += 1
    else:
      merged_arr.append(arr2[k])
      k += 1

  # append if leftover
  if i <= len(arr1):
    merged_arr.extend(arr1[i:arr1_len])
  if k <= len(arr2):
    merged_arr.extend(arr2[k:arr2_len+1])
  # reassign into input arrays
  arr1 = merged_arr[0:(arr1_len)+1]
  arr2 = merged_arr[arr2_len+1:arr1_len+arr2_len+2]

  return merged_arr, arr1, arr2

print('a first thought solution:', merge_sorted_arrays([1, 3, 4, 5],[2, 4, 6, 8]))

# note to self, first i solved this proble with what i thought was a naive approach but after 
# checking this is the preferred algo, i just need to clean up execution/code
