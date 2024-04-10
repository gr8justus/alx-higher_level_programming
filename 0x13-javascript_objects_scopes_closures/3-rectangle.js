#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (arguments.length < 2 || w <= 0 || h <= 0) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let height = 0; height < this.height; height++) {
      for (let width = 0; width < this.width; width++) {
        if (width === this.width - 1) {
          console.log('X');
        } else {
          process.stdout.write('X');
        }
      }
    }
  }
}

module.exports = Rectangle;
