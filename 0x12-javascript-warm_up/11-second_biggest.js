#!/usr/bin/node
// searches the second biggest int passed as an arg
let argv = process.argv;
let i = 0;
let newa = [];
if ((argv.length < 4 && parseInt(argv[2]) >= 0) || !argv[2]) {
  console.log('0');
} else {
  for (i = 2; i < argv.length; i++) {
    newa.push(parseInt(argv[i]));
  } newa = [...new Set(newa)].sort((a, b) => a - b);
  console.log(newa[newa.length - 2]);
}
