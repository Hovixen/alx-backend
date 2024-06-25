/*
 * Node Redis client publisher script
 */

import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Handle connection event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle error event
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Publish a message to a channel after a specified time.
 * @param {string} message - The message to publish.
 * @param {number} time - The delay in milliseconds before publishing the message.
 */
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
}

// Call the function to publish messages
publishMessage('Holberton School', 100);
publishMessage('Holberton School San Francisco', 200);
publishMessage('KILL_SERVER', 300);
publishMessage("Holberton Student #3 starts course", 400);
