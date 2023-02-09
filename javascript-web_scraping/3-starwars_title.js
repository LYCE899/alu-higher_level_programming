#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('An error has occurred');
  }
});
