#!/usr/bin/node
// uses a get request to desplay a status code
let r = require('request');
r(process.argv[2], function (error, r) {
  if (!error) {
    console.log('code: ' + r.statusCode);
  } else {
    console.log(error);
  }
});
