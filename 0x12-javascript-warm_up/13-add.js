#!/usr/bin/node

// Define the add function to return the addition of two integers
function add(a, b) {
  return a + b;
}

// Export the add function to make it visible from outside
module.exports = {
  add: add
};
