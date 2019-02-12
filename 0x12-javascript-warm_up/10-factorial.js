#!/usr/bin/node
// computes and prints a factorial
let input = parseInt(process.argv[2]);
let i = 0;
if (isNaN(input) || input <= 1) {
  console.log('1');
} else {
  let out = input;
  for (i = 0; input > 1; i++) {
    input = input - 1;
    out *= input;
  }
  console.log(out);
}
