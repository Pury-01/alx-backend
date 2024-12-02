// add setNewSchool and displaySchoolValue functions
// Node Redis Client
import redis from 'redis';
import { createClient } from 'redis';
import { promisify } from 'util';

// create a redis client
const client = createClient();

// Event for connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event for error
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// function to set a new value
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// function to display the value of a given key
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(vlaue);
  } catch (err) {
      console.log(`Error getting value for ${schoolName}: ${err.message}`);
  }
}

// call the functions
(async () => {
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
})();
