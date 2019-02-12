#!/usr/bin/node
// prints weather arguments were found
let argc = process.argv.length;
if (argc === 2) {
  console.log('No argument');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
