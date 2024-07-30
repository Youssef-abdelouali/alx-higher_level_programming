#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value++;
  }
};

console.log(myObject);

// Add the incr function
myObject.incr = function () {
  this.value++;
};

// Call incr and print the object
myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
