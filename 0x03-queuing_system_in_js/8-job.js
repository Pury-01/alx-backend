import kue from 'kue';

const queue = kue.createQueue();

export default function createPushNotificationsJobs(jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Iterate over each job data and create a job
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData);
    
    if (!job) {
      console.error('Error creating job');
      return;
    }

    // Attach event listeners
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    })
    .on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    })
    .on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    })
    .on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Save the job to the queue
    job.save((err) => {
      if (err) {
        console.error(`Failed to save job: ${err}`);
      }
    });
  });
}
