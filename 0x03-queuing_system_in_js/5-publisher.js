// Node Redis client
import { createClient} from 'redis';

// create a Redis client
const client = createClient();

// event for connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// event for error
client.on('error', (err) => {
  console.log(`Reddis client not connected to the server: ${err.message}`);
});

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
}

// call the function with various messages and delays
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
