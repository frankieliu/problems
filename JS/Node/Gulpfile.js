// gist.github.com/danharper/3ca2273125f500429945
// New ES6 project with Babel, Browserify & Gulp
var fs = require('fs');
var gulp = require('gulp');
var connect = require('gulp-connect');
var browserify = require('browserify');
var babelify = require('babelify');

gulp.task('connect', function() {
  connect.server({
    root: 'app',
    livereload: true
  });
});
 
gulp.task('html', function () {
    console.log('html');
    gulp.src('./app/*.html')
	.pipe(gulp.dest('./app'))
	.pipe(connect.reload());
});

gulp.task('browserify', function() {
    console.log('In browserify');
    var bf = fs.createWriteStream(__dirname + '/app/scripts/js/app.js');
    var b = browserify('./app/src/js/app.js')
	.transform(babelify)
	.bundle()
	.pipe(bf);

    /*
    var b = browserify('./app/src/js/app.js')
	.transform(babelify);
    /*	{
	    entries: './app/src/js/app.js',
	    debug: !gulp.env.production,
	    insertGlobals: true,
	    transform : [ babelify ]
		//[ .configure({ 'presets': ['es2015','stage-0'] }) ]
	});
    // b.add('./app/src/js/app.js');

    return b.bundle()
	.pipe(gulp.dest('./app/scripts/js/'));
*/
});

gulp.task('watch', function () {
    gulp.watch(['./app/*.html'], ['html']);
    gulp.watch(['./app/src/**/*.js'], ['browserify']);
});
 
gulp.task('default', ['connect', 'watch']);
