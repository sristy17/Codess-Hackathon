var express = require('express');
var app = express();

app.set('view engine', 'ejs');


// Home page
app.get('/', function(req, res) {
res.render('pages/home.ejs');
});


//About page
app.get('/about', function(req, res) {
res.render('pages/about.ejs');
});

//Community page
app.get('/community', function(req, res) {
res.render('pages/community.ejs');
});

//Helpline page
app.get('/helpline', function(req, res) {
res.render('pages/helpline.ejs');
});


app.listen(3000);
console.log('Server is listening on port 3000');