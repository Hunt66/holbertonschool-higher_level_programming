#!/usr/bin/node
// esrever func
exports.esrever = function (list) {
  let i = list.length;
  let newlst = [];
  for (i = i - 1; i >= 0; i--) {
    newlst.push(list[i]);
  }
  return newlst;
};
