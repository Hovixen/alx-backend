import kue from 'kue';

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

/**
 * Send a notification.
 * @param {string} phoneNumber - The phone number to send the notification to.
 * @param {string} message - The message to send.
 * @param {object} job - The job object.
 * @param {function} done - The callback function to call when the job is done.
 */
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  job.progress(100, 100);
  done();
}

// Create a Kue queue
const queue = kue.createQueue();

// Process jobs in the 'push_notification_code_2' queue, 2 jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

