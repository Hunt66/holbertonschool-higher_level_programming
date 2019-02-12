#!/usr/bin/node
// prints a square based on given arg or missing size if no size given
let size = parseInt(process.argv[2]);
let i = 0;
let x = 'X';
if (size) {
  for (i = 0; i < size; i++) {
    console.log(x.repeat(size));
  }
} else {
  console.log('Missing size');
}
