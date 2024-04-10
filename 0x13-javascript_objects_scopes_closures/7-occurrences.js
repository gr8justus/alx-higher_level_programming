#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;

  list.forEach((member) => {
    if (member === searchElement) {
      occurences++;
    }
  });
  return occurences;
};
