/*
 * script connects to redis server
 */

import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
const asyncGet = promisify(client.get).bind(client);

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


async function displaySchoolValue(schoolName) {
  try {
    const value = await asyncGet(schoolName);
    console.log(value);
  } catch (err) {
    console.log(`Error retrieving value for ${schoolName}: ${err.message}`);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
