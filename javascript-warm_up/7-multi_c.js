#!/usr/bin/node

const firstArg = process.argv[2];
const number = parseInt(firstArg, 10);
if (Number.isInteger(number)) {
  let i = 0;
  while (i < number) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}