#!/usr/bin/node
// this contains the square class

const Square0 = require('./5-Square');

class Square extends Square0 {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let p = '';
    let i = 0;
    let j = 0;
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        p += c;
      } console.log(p);
      p = '';
    }
  }
}
module.exports = Square;
