#!/usr/bin/node
const str = 'C is fun';
const intBase = 10;
const iterations = parseInt(process.argv[2], intBase);

if (isNaN(iterations)) {
  console.log('Missing number of occurrences');
} else if (iterations > 0) {
  for (let iterator = 0; iterator < iterations; iterator++) {
    console.log(str);
  }
}
