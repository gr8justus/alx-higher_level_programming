#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  const nbElements = list.length;

  for (let element = nbElements - 1; element >= 0; element--) {
    reversedList.push(list[element]);
  }
  return reversedList;
};
