#!/usr/bin/node
// func that increments and calls a func
exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
