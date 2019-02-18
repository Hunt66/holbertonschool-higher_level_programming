#!/usr/bin/node
let dict = require('./101-data.js').dict;
let ndict = {};
for (let key in dict) {
  if (ndict[dict[key]] === undefined) {
    ndict[dict[key]] = [];
  }
  ndict[dict[key]].push(key);
}
console.log(ndict);
