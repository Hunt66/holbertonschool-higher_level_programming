#!/usr/bin/node
// Prints my number: <the number> or not a number if not
let num = parseInt(process.argv[2]);
if (num) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
