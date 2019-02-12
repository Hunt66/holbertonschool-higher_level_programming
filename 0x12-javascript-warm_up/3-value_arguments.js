#!/usr/bin/node
// prints weather arguments were found
let argv = process.argv[2];
if (argv) {
  console.log(argv);
} else {
  console.log('No argument');
}
