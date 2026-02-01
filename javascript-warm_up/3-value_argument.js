#!/usr/bin/node

let count = 0;
process.argv.forEach(() => {
  count++;
});

if (count === 2 || count < 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}