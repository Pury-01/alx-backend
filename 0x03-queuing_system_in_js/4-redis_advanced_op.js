// Node Redis Client
import redis from 'redis';
import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Event for connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event for error
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Create Hash
const hashKey = 'HolbertonSchools';
const schools = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

// store hash using hset
for (const [field, value] of Object.entries(schools)) {
  client.hset(hashKey, field, value, redis.print);
}

// Display the hash using hgetall
client.hgetall(hashKey, (err, res) => {
  if (err) {
    console.error(`Error retrieving hash: ${err.message}`);
  } else {
    console.log(res);
  }
});
