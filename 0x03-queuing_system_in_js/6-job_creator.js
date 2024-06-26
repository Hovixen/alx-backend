/*
 * creating the job creator using kue
 */

import kue from 'kue';

const queue = kue.createQueue();

const data = {
  phonenumber: "123456987",
  message: "message"
}

const job = queue.create('push_notification_code', data)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.log('Error creating job:', err);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
