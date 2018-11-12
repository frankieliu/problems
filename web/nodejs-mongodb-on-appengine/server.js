'use strict';

const mongodb = require('mongodb');
const http = require('http');
const nconf = require('nconf');

// Read in keys and secrets. Using nconf use can set secrets via
// environment variables, command-line arguments, or a keys.json file.
nconf.argv().env().file('keys.json');

// Connect to a MongoDB server provisioned over at
// MongoLab.  See the README for more info.

const user = nconf.get('mongoUser');
const pass = nconf.get('mongoPass');
const host = nconf.get('mongoHost');
const port = nconf.get('mongoPort');

let uri = nconf.get('mongoUri');
// if (nconf.get('mongoDatabase')) {
//  uri = `${uri}/${nconf.get('mongoDatabase')}`;
//}
console.log(uri);

mongodb.MongoClient.connect(uri, {useNewUrlParser: true}, (err, client) => {
  if (err) {
    throw err;
  }

  // Create a simple little server.
  http.createServer((req, res) => {
    if (req.url === '/_ah/health') {
      res.writeHead(200, {
        'Content-Type': 'text/plain'
      });
      res.write('OK');
      res.end();
      return;
    }
    // Track every IP that has visited this site
    const db = client.db('test');
    const collection = db.collection('IPs');

    const ip = {
      address: req.connection.remoteAddress
    };

    collection.insert(ip, (err) => {
      if (err) {
        throw err;
      }

      // push out a range
      let iplist = '';
      collection.find().toArray((err, data) => {
        if (err) {
          throw err;
        }
        data.forEach((ip) => {
          iplist += `${ip.address}; `;
        });

        res.writeHead(200, {
          'Content-Type': 'text/plain'
        });
        res.write('IPs:\n');
        res.end(iplist);
      });
    });
  }).listen(process.env.PORT || 8080, () => {
    console.log('started web process');
  });
});
