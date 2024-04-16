#!/usr/bin/node

const argIndex = 2;
const size = process.argv[argIndex];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let height = 0; height < size; height++) {
    for (let width = 0; width < size; width++) {
      if (width === size - 1) {
        console.log('X');
      } else {
        process.stdout.write('X');
      }
    }
  }
}
