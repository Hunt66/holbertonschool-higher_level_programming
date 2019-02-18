#!/usr/bin/node
// Simply an empty class Rectangle with nothing?

class Rectangle {
  constructor (w, h) {
    if (h <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    }
    this.height = h;
    this.width = w;
  }
}
module.exports = Rectangle;
