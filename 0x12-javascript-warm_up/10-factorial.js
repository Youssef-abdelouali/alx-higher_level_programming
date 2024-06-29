#!/usr/bin/node

// Define a recursive function to compute the factorial
function factorial (n) {
  // Base case: factorial of 0 or 1 is 1
  if (n === 0 || n === 1) {
    return 1;
  }
  // Recursive case: compute factorial by multiplying n with factorial of (n - 1)
  return n * factorial(n - 1);
}

// Extract the argument from process.argv and parse it as an integer
const arg = parseInt(process.argv[2]);

// Check if the argument is NaN (Not a Number)
if (isNaN(arg)) {
  console.log(1);
} else {
  // Compute the factorial and print the result
  console.log(factorial(arg));
}
