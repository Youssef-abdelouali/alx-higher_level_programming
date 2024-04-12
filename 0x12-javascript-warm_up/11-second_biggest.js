#!/usr/bin/node

// Extract the arguments from process.argv and remove the first two elements (script name and interpreter)
const args = process.argv.slice(2);

// Check if no arguments are passed or only one argument is passed
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  // Convert the arguments to integers and sort them in ascending order
  const numbers = args.map(Number).sort((a, b) => a - b);

  // Print the second last element, which is the second biggest integer
  console.log(numbers[numbers.length - 2]);
}
