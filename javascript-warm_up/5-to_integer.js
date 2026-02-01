#!/usr/bin/node

const firstArgument = process.argv[2];
const number = parseInt(firstArgument, 10);
if (Number.isInteger(number)) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}