#!/usr/bin/node
// logme func
let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
