var express = require('express');
var app = express();

app.set('view engine', 'ejs');


// Home page
app.get('/', function(req, res) {
res.render('Pages/Home.ejs');
});



app.listen(3000);
console.log('Server is listening on port 3000');