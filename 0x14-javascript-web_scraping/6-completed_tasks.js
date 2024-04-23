#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  // Count completed tasks for each user
  tasks.forEach(function(task) {
    if (task.completed) {
      const userId = task.userId;
      completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
    }
  });

  // Output the results
  console.log(completedTasksByUser);
});

