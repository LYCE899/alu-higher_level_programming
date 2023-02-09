#!/usr/bin/node
// Retrieving a character from the URL using JavaScript
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  type: 'GET',
  success: (result) => {
    $('#character').text(result.name);
  }
});
