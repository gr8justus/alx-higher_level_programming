#!/usr/bin/node

const argIndex = 2;
const num = process.argv[argIndex];

function factorial (n) {
  let result;

  if (isNaN(n) | n <= 1) { // Base condition
    result = 1;
  } else {
    result = n * factorial(n - 1);
  }
  return result;
}

console.log(factorial(num));
