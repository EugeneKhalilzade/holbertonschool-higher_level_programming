#!/usr/bin/node

function secondBiggest (array) {
  if (array.length === 0 || array.length === 1) {
    return 0;
  } else {
    const sortedArray = array.sort((a, b) => a - b);
    return sortedArray[sortedArray.length - 2];
  }
}

const argsArray = process.argv.slice(2).map(Number);
console.log(secondBiggest(argsArray));