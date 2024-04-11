#!/usr/bin/node

let nbArgPrinted = 0;

exports.logMe = function (item) {
  console.log(`${nbArgPrinted}: ${item}`);
  nbArgPrinted++;
};
