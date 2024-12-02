# Queuing system in JS
This project involves building a Redis-based queuing system with Node.js and Express.js, leveraging Redis for data storage and the Kue library for managing job queues.

## Learning Objectives
- Set up annd run a Redis server on the local machine.
- Use the Redis client for basic and advanced operations.
- Integrate Redis with Node.js using callbacks and async/await patterns.
- Build a simple Express.js application that interacts with Redis.
- Build a simple Express.js appplication that interacts with Redis.
- Utilize Kue to manage job queues and process background jobs.
- Establish a basic publisher-subscriber pattern using Redis.

## Requirements
- Ubuntu 18.04 LTS
- Node.js 12.x
- Redis 5.0.7+
- Use ES^ syntax with Baabel for transpiling
- Files should have a .js extension

### Tools
- Redis
- Kue(Queue library)
- Express.js

## Setup
1. Install Redis
Download and compile the latest Redis version(> 5.0.7):
```
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz  
$ tar xzf redis-6.0.10.tar.gz  
$ cd redis-6.0.10  
$ make  
```

Start the Redis server:
```
$ src/redis-server &
```

Verify the setup:
```
$ src/redis-cli ping  
PONG  
```

2. Set up Node.js Environment:
Install project dependencies:
```
$ npm install
```

3. Run Redis Commands:
- set and retrieve a value:
```
127.0.0.1:[Port]> set Holberton School  
127.0.0.1:[Port]> get Holberton  
```

- Run Node.js scripts
```
$ npm run dev <filename.js>
```
