#!/usr/bin/node
// prints c is fun argv number of times
let i = 0;
for (i = 0; i < parseInt(process.argv[2]); i++) {
  console.log('C is fun');
}
