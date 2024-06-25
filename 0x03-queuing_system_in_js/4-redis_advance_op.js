/*
 * script connects to redis server
 */

import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to server');
});

client.on('error', (err) => {
  console.log(`Redis not connected to the server: ${err}`);
});


/*
 * function stores hashed values in redis
 */

function createHash () {
  client.hset('HolbertonSchools', 'Portland', 50, print);
  client.hset('HolbertonSchools', 'Seattle', 80, print);
  client.hset('HolbertonSchools', 'New York', 20, print);
  client.hset('HolbertonSchools', 'Bogota', 20, print);
  client.hset('HolbertonSchools', 'Cali', 40, print);
  client.hset('HolbertonSchools', 'Paris', 2, print);
}


function displayHashValue() {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.log(`Error retrieving value for ${schoolName}: ${err.message}`)
    } else {
      console.log(reply);
    }
  });
}

createHash();
displayHashValue();
