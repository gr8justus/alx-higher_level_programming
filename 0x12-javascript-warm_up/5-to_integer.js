#!/usr/bin/node
const argIndex = 2;
const intBase = 10;
const convertedArg = parseInt(process.argv[argIndex], intBase);

if (!isNaN(convertedArg)) {
  console.log(`My number: ${convertedArg}`);
} else {
  console.log('Not a number');
}
