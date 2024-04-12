#!/usr/bin/node

// Extract the first argument from process.argv
const arg = process.argv[2];

// Convert the argument to an integer using parseInt
const num = parseInt(arg);

// Check if the argument can be converted to an integer
if (!isNaN(num)) {
  console.log("My number:", num);
} else {
  console.log("Not a number");
}
