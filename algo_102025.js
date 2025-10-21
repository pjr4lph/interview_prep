/**
 * @param {number[][]} brackets
 * @param {number} income
 * @return {number}
 */
const calculateTax = function(brackets, income) {
    // start time 4:05pm, finish 5:15pm
    // create vars for taxes and current income
    // iterate through brackets array
    // before calculating, check if curr is greater than upper 
    // calculate tax at bracket
    // if at 0, calculate tax accordingly
    let taxes = 0;
    let currentInc = income;
    for (let i = 0; i < brackets.length; i++) {
        if (currentInc > 0) {
            if (i === 0) {
                currentInc = currentInc - brackets[i][0];
                taxes = brackets[i][0] * (brackets[i][1] / 100);
            } else {
                currentBracketAmount = brackets[i][0] - brackets[i-1][0];
                lessCurrent = Math.min(currentBracketAmount, currentInc);
                taxes = taxes + (lessCurrent * (brackets[i][1] / 100));
                currentInc = currentInc - currentBracketAmount;
            }
        }
    }
    return taxes;
};

console.log(calculateTax([[3,50],[7,10],[12,25]], 10), '---> 2.6500');