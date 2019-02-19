#!/usr/bin/node
// counts the number of tasks completed by user id
let r = require('request');
r(process.argv[2], function (error, result, body) {
  if (!error) {
    let lst = JSON.parse(body);
    let out = {};
    let i = 0;
    for (i = 0; i < lst.length; i++) {
      if (lst[i]['completed'] === true) {
        if (out[lst[i]['userId']] !== undefined) {
          out[lst[i]['userId']] += 1;
        } else {
          out[lst[i]['userId']] = 1;
        }
      }
    }
    console.log(out);
  } else {
    console.log(error);
  }
});
