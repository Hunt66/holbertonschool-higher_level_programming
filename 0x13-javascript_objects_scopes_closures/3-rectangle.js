#!/usr/bin/node
// Simply an empty class Rectangle with nothing?

class Rectangle {
  constructor (w, h) {
    if (h <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    }
    this.width = w;
    this.height = h;
  }
  print () {
    let p = '';
    let i = 0;
    let j = 0;
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        p += 'X';
      } console.log(p);
      p = '';
    }
  }
}
module.exports = Rectangle;
