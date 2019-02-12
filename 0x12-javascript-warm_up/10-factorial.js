#!/usr/bin/node
// computes and prints a factorial

function fact (x) {
  if (isNaN(x) || x <= 1) {
    return 1;
  } else {
    return x * fact(x - 1);
  }
}
let input = parseInt(process.argv[2]);
console.log(fact(input));
