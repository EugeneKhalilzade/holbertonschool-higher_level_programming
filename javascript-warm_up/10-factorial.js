#!/usr/bin/node

function factorial (number) {
  if (isNaN(number) || number <= 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

const firstArg = parseInt(process.argv[2], 10);
console.log(factorial(firstArg));
