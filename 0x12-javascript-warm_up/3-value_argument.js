#!/usr/bin/node
const args = process.argv;
const firstArgIndex = 2;

if (!args[firstArgIndex]) {
  console.log('No argument');
} else {
  console.log(args[firstArgIndex]);
}
