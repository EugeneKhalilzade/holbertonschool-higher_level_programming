#!/usr/bin/node

const firstArg = process.argv[2];
const number = parseInt(firstArg, 10);
if (Number.isInteger(number)) {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
} else {
  console.log('Missing size');
}
