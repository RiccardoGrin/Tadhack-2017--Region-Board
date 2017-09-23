var express = require('express');
var router = express.Router();

var request = require('request');
/* GET home page. */
router.get('/', function(req, res, next) {

  res.render('index', { title: 'Region Board' });

  // var header = {
  //   "Content-Type": 'application/json',
  //   "Authorization": 'acc99bff885-b870-31b1-9e38-7a356afd9ea9:aut0d3fd9f0-bc72-357f-800d-f5a0607dde31'
  // }

  // var authorization = "acc99bff885-b870-31b1-9e38-7a356afd9ea9:aut0d3fd9f0-bc72-357f-800d-f5a0607dde31";

  // // SID = "acc99bff885-b870-31b1-9e38-7a356afd9ea9"
  // // Token = "aut0d3fd9f0-bc72-357f-800d-f5a0607dde31"
  // var data = {
  //   from: '61476857588',
  //   to: '61497113108',
  //   text: 'Hello'
  // }

  // var options = {
  //   url: 'https://api.apifonica.com/v2/accounts/acc99bff885-b870-31b1-9e38-7a356afd9ea9/messages',
  //   method: 'POST',
  //   headers: header,
  //   body: data
  //   //authentication: 'acc99bff885-b870-31b1-9e38-7a356afd9ea9:aut0d3fd9f0-bc72-357f-800d-f5a0607dde31'
  // }

  // // request.post('https://api.apifonica.com/v2/accounts/acc99bff885-b870-31b1-9e38-7a356afd9ea9/messages', { headers: header, formData: data }, function (err, fonicaRes, body) {
  // //   if (err) {
  // //     return console.error('post failed:', err);
  // //   }
  
  // //   console.log('Post successful!  Server responded with:', body);
  // // });

  // var fonicaReq = request('https://api.apifonica.com/v2/accounts/acc99bff885-b870-31b1-9e38-7a356afd9ea9/messages', options, function(fonicaRes) {
  //   console.log(fonicaRes);
  // });
});

module.exports = router;
