#!/usr/bin/node
// gets contents of a webpage and stores it in a file
let r = require('request');
let fs = require('fs');
r(process.argv[2], function (error, result, body) {
  if (!error) {
    fs.writeFile(process.argv[3], body, function (error2) {
      if (error2) {
        console.log(error2);
      }
    });
  } else {
    console.log(error);
  }
});
