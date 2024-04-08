#!/usr/bin/node
const pathCount = 2;
const argsCount = (process.argv).length - pathCount;

if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log('Argument found');
} else if (argsCount >= 2) {
  console.log('Arguments found');
}
