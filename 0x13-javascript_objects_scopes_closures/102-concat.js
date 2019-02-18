#!/usr/bin/node
let fs = require('fs');
if (process.argv.length === 5) {
  let a = fs.readFileSync('./' + process.argv[2]);
  let b = fs.readFileSync('./' + process.argv[3]);
  fs.writeFileSync(process.argv[4], a + b);
}
