// job processor
import kue from 'kue';

// create queue from kue
const queue = kue.createQueue();

// function that sends notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// queue process that listens to new jobs
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;

	// call the sendNotification function
	sendNotification(phoneNumber, message);

	// indicate the job is done
	done();
});
