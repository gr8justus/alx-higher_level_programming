#!/usr/bin/node

const argsLen = (process.argv).length;
let result;

if (argsLen <= 3) {
  result = 0;
} else {
  (process.argv).sort();
  result = process.argv[argsLen - 2];
}

console.log(result);
