#!/usr/bin/node

// Extract the first argument from process.argv
const arg = process.argv[2];

// Convert the argument to an integer using parseInt
const num = parseInt(arg);

// Check if the argument can be converted to a positive integer
if (!isNaN(num) && num > 0) {
  // Loop x times and print "C is fun" each time
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
