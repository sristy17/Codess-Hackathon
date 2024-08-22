var express = require('express');
var app = express();

app.set('view engine', 'ejs');

// Home page
app.get('/', function(req, res) {
    res.render('pages/home.ejs');
});

// About page
app.get('/about', function(req, res) {
    res.render('pages/about.ejs');
});

// Community page
app.get('/community', function(req, res) {
    res.render('pages/community.ejs');
});

// Helpline page
app.get('/helpline', function(req, res) {
    res.render('pages/helpline.ejs');
});

// Donation page
app.get('/donation', function(req, res) {
    res.render('pages/donation.ejs');
});

// Submit Story page
app.get('/submit-story', function(req, res) {
    res.render('pages/submit-story.ejs');
});

// Job Application page
app.get('/job-application', function(req, res) {
    res.render('pages/job-application.ejs');
});

app.listen(3000);
console.log('Server is listening on port 3000');