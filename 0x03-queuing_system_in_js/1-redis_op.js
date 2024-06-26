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
 * function sets parameter in redis
 * @param: schoolName(key)
 * @param: value
 */

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, print);
}


function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(`Error retrieving value for ${schoolName}: ${err.message}`)
    } else {
      console.log(reply);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
