var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var index = require('./routes/index');
var users = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', index);
app.use('/users', users);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

app.post('/message', function(req, res) {
  console.log('Messages accessed');
  res.setHeader('Content-Type', 'application/json');
  //mimic a slow network connection
  setTimeout(function(){
      res.send(JSON.stringify({
          message_sid: req.body.message_sid || null,
          account_sid: req.body.account_sid || null,
          from: req.body.from || null,
          to: req.body.to || null,
          text: req.body.text || null,
          status: req.body.status || null
      }));
  }, 1000)

  //debugging output for the terminal
  console.log('you posted: ' + req.body.text + ', from ' + req.body.from);
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

var port = 3000;
app.listen(port);
console.log('Listening at http://localhost:' + port)

module.exports = app;
