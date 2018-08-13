var Pusher = require('pusher');

var pusher = new Pusher({
  appId: '576138',
  key: '1a7ba71c28d60c37f2b0',
  secret: '74dd0bd14e021de9fdd0',
  cluster: 'us2',
  encrypted: true
});

pusher.trigger('my-channel', 'my-event', {
  "message": "hello world"
});
