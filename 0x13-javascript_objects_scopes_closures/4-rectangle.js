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

  rotate () {
    const newWidth = this.height;
    const newHeight = this.width;

    this.width = newWidth;
    this.height = newHeight;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
