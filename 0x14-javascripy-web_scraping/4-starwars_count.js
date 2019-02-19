#!/usr/bin/node
// prints the number of moveis where the character Wedge Antilles apperes
// takes the starwars api website
let r = require('request');
r(process.argv[2], function (error, response, body) {
  let count = 0;
  let i = 0;
  let j = 0;
  if (!error) {
    let inn = JSON.parse(body).results;
    for (i = 0; i < inn.length; i++) {
      for (j = 0; j < inn[i].characters.length; j++) {
        if (inn[i].characters[j].includes('18')) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
