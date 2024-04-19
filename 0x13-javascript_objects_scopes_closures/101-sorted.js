#!/usr/bin/node
const { dict } = require('./101-data');

const sortedDict = {};
for (let userId in dict) {
  const occurrences = dict[userId];
  if (!sortedDict[occurrences]) {
    sortedDict[occurrences] = [];
  }
  sortedDict[occurrences].push(userId);
}

console.log(sortedDict);
