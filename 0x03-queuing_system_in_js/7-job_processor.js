// job processor
import kue from 'kue';

// blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// sendNotification function
const sendNotification = (phoneNumber, message, job, done) => {
  // track progress: 0%
  job.progress(0, 100);

  // check if phone number is blacklisted
  if (balcklistedNumbers.include(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track progress: 50%
  job.progress(50, 100);

  // simulate sending the notification
  console.log(`Sending notification to ${phoneNumber}, with message ${message}`);

  // complete the job
  done();
};

  // create queue with kue
  const queue = kue.createQueue();

  // process jobs in the `push_notification_code_2` queue
  queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
  });
