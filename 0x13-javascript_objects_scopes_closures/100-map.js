#!/usr/bin/node
let lst = require('./100-data.js').list;
let nlst = [];
console.log(lst);
nlst = lst.map((num, index) => num * index);
console.log(nlst);
