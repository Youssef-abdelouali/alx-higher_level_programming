#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
