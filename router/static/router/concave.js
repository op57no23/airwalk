var turf = require('@turf/turf');
var fs = require('fs');

var blackCarbon = JSON.parse(fs.readFileSync('BlackCarbon.json'));

var sf = JSON.parse(fs.readFileSync('sfpolygon.json'));
