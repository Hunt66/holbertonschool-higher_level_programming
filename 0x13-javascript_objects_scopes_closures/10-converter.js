#!/usr/bin/node
// coverter func

exports.converter = function (base) {
  function conv (num) {
    return num.toString(base);
  }
  return conv;
};
