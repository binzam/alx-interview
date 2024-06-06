#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi-api.alx-tools.com/api/';

const getCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response && response.statusCode === 200) {
        const characterName = JSON.parse(body).name;
        resolve(characterName);
      }
    });
  });
};
const getMovieCharacters = (movieId) => {
  return new Promise((resolve, reject) => {
    request(`${API_URL}films/${movieId}`, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response && response.statusCode === 200) {
        const charactersURL = JSON.parse(body).characters;
        const characterPromises = charactersURL.map((url) =>
          getCharacterName(url)
        );
        Promise.all(characterPromises)
          .then((characters) => resolve(characters))
          .catch((error) => reject(error));
      }
    });
  });
};
const movieId = process.argv[2];
if (process.argv.length > 2) {
  getMovieCharacters(movieId)
    .then((characters) => {
      console.log(characters.join('\n'));
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}
