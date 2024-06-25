/*
 * script connects to redis server
 */

import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to server');
});

client.on('error', (err) => {
  console.log(`Redis not connected to the server: ${err}`);
});
