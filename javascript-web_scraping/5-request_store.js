#!/usr/bin/node
// Writing a script that gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);
request(args[0], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(args[1], body, (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
