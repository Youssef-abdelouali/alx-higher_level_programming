#!/usr/bin/node

// Extract the first argument from process.argv
const arg = process.argv[2];

// Convert the argument to an integer using parseInt
const size = parseInt(arg);

// Check if the argument can be converted to a positive integer
if (!isNaN(size) && size > 0) {
  // Loop to print each row of the square
  for (let i = 0; i < size; i++) {
    // Print a row of X's with the specified size
    console.log('X'.repeat(size));
  }
} else {
  console.log("Missing size");
}
