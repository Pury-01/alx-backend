// Node Redis Client
import { createClient } from 'redis';

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
