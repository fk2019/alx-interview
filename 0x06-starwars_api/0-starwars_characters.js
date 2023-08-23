#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (err, response, body) => {
  if (err) console.log(err);
  const data = JSON.parse(body).characters;
  const dataPromise = data.map(
    (url) => new Promise((resolve, reject) => {
      request(url, (promiseErr, __, dataBody) => {
        if (promiseErr) reject(promiseErr);
        resolve(JSON.parse(dataBody).name);
      });
    })
  );
  Promise.all(dataPromise)
    .then((name) => console.log(name.join('\n')))
    .catch((err) => console.log(err));
});
