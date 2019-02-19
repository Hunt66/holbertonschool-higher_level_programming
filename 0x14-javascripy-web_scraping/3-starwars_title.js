#!/usr/bin/node
// prints the title of a starwars movei given the episode number (by how they
// are made not chronologicly)
let r = require('request');
r('http://swapi.co/api/films/' + process.argv[2], function (error, r, body) {
  if (!error) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(error);
  }
});
