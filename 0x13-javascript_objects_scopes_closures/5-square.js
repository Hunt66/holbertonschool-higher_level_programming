#!/usr/bin/node
// this contains the square class

module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
};
