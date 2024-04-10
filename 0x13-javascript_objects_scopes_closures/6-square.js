#!/usr/bin/node

const Square0 = require('./5-square.js');

class Square extends Square0 {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let height = 0; height < this.height; height++) {
        for (let width = 0; width < this.width; width++) {
          if (width === this.width - 1) {
            console.log(c);
          } else {
            process.stdout.write(c);
          }
        }
      }
    }
  }
}

module.exports = Square;
