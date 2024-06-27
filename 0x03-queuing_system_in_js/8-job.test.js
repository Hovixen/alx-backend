import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from '../8-job.js';

// Create a queue instance
const queue = kue.createQueue();

describe('createPushNotificationsJobs', function() {
  // Enter test mode before running tests
  before(() => {
    kue.Job.queue = queue;
    queue.testMode.enter();
  });

  // Clear the queue and exit test mode after tests are done
  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  // Clear the queue before each test
  beforeEach(() => {
    queue.testMode.clear();
  });

  it('should throw an error if jobs is not an array', function() {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should create jobs and add them to the queue', function() {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });

  it('should log appropriate messages for job events', function(done) {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' }
    ];

    // Temporarily replace console.log to capture log messages
    const logs = [];
    const originalLog = console.log;
    console.log = (msg) => logs.push(msg);

    createPushNotificationsJobs(jobs, queue);

    const job = queue.testMode.jobs[0];

    // Simulate job events
    job._events.complete();
    job._events.failed('Some error');
    job._events.progress(50);

    // Allow some time for async logs
    setTimeout(() => {
      expect(logs).to.include(`Notification job created: ${job.id}`);
      expect(logs).to.include(`Notification job ${job.id} completed`);
      expect(logs).to.include(`Notification job ${job.id} failed: Some error`);
      expect(logs).to.include(`Notification job ${job.id} 50% complete`);

      // Restore original console.log
      console.log = originalLog;
      done();
    }, 50);
  });
});
