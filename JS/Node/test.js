// gist.github.com/danharper/3ca2273125f500429945
// New ES6 project with Babel, Browserify & Gulp
var gulp = require('gulp');
var connect = require('gulp-connect');
var browserify = require('browserify');
var babelify = require('babelify');

var b = browserify('./app/src/js/app.js')
    .transform(babelify)
    .bundle()
    .pipe(process.stdout);
