const plusOne = function(digits) {
    // understanding that base case scenario, all digits are less than 9 and that worse case scenario all digits can be 9
    // plan of action, iterate backwards through digits and check for 9
    // if 9, carry 1 to the next number and set to 0
    // if not 9, add 1
    if (digits[digits.length-1] < 9) {
        digits[digits.length-1] = digits[digits.length-1] + 1;
    } else {
    // create a while loop which is truthy on a carry value
        let carry = 1;
        let i = digits.length-1;
        while (carry > 0) {
            if (digits[i] === 9 && i === 0) {
              digits[i] = 0;
              digits.unshift(1);
              carry = 0;
            } else if (digits[i] === 9) {
                digits[i] = 0;
                carry = 1;
            } else if (digits[i] < 9) {
                digits[i] = digits[i] + 1;
                carry = 0;
            }
            i--;
        }
    }
    return digits;
};

// console.log(plusOne([1,2,3]), 'should equal --> [1,2,4]');
// console.log(plusOne([1,2,9]), 'should equal --> [1,3,0]');
// console.log(plusOne([1,9,9]), 'should equal --> [2,0,0]');
// console.log(plusOne([3,9,9,9]), 'should equal --> [4,0,0,0]');
// console.log(plusOne([9,9,9,9]), 'should equal --> [1,0,0,0,0]');

function palindrome(string) {
  let left = 0;
  let right = string.length-1;
  while (left < right) {
    if (string[left] !== string[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
}

console.log(palindrome('racecar'), '--> true');
console.log(palindrome('raceXcar'), '--> false');