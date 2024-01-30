#!/usr/bin/node

// Script that uses the request module to make a GET request
// to the Star Wars API endpoint and then filter the films
// where the character "Wedge Antilles"

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;
const movieId = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body);
    const filmsWithWedge = filmsData.results.filter(film =>
      film.characters.includes(movieId)
    );
    console.log(filmsWithWedge.length);
  }
});
