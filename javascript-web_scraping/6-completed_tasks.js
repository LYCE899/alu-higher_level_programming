#!/usr/bin/node
// Writing a script that computes the number of tasks completed by user id.
const request = require('request');

function getCompletedTasks (data, userId) {
  let count = 0;
  data
    .filter((element) => element.userId === userId)
    .forEach((task) => {
      if (task.completed) {
        count++;
      }
    });
  return count;
}

const url = process.argv[2];

const results = {};
request.get(url, (error, response) => {
  if (error) {
    throw error;
  }
  const data = JSON.parse(response.body);
  data.forEach((element) => {
    if (!(element.userId in results)) {
      if (getCompletedTasks(data, element.userId) > 0) {
        results[element.userId] = getCompletedTasks(data, element.userId);
      }
    }
  });
  console.log(results);
});
