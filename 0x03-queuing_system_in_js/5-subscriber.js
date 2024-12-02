// Node Redis Client
import redis from 'redis';
import { createClient } from 'redis';

// create a Redis client
const client = createClient();

// Event for connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event for error
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the channel
const channel = 'holberton school channel';
client.subscribe(channel);

// handle messsages
client.on('message', (channel, message) => {
  console.log(message);

// check for the KILL_SERVER message
if (message === 'KILL_SERVER') {
  client.unsubscribe(channel);
  client.quit();
}
});
