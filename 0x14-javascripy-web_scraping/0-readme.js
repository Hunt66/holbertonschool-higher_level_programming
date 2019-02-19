#!/usr/bin/node
// script reading and printing the contents of a file
let fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (error, content) {
  if (!error) {
    console.log(content);
  } else {
    console.log(error);
  }
});
