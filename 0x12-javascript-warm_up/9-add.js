#!/usr/bin/node

// Define a function add with two parameters a and b
function add(a, b) {
  // Parse the arguments as integers and calculate the sum
  const sum = parseInt(a) + parseInt(b);

  // Check if the result is NaN (Not a Number)
  if (isNaN(sum)) {
    console.log("NaN");
  } else {
    // Print the sum
    console.log(sum);
  }
}

// Extract the arguments from process.argv
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Call the add function with the provided arguments
add(arg1, arg2);
