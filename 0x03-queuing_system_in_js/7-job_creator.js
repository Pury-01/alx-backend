// create jobs
import kue from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

// create queue with kue
const queue = kue.createQueue();

// loop through job array and create jobs in the queue
jobs.forEach((jobData) => {
  const job = queue.create('push_notification-code_2', jobData);
  
  // log when job is created
  job
    .on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    })
     .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
     })
      .on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${errr}`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });

    // save the job to the queue
    job.save((err) => {
      if (err) {
        console.error(`Failed to create job: ${err}`);
      }
    });
});
