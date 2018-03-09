module.exports = function(grunt) {
    grunt.initConfig({
	pkg: grunt.file.readJSON('package.json'),
	browserify: {
	    main: {
		options: {
		    browserifyOptions: {
			debug: true
		    }
		    // , transform: [[“babelify”, { “stage”: 1 }]]
		},
		src: 'src/app.js',
		dest: 'scripts/app.js'
	    }
	},
	watch: {
	    files: [ 'src/**/*.js' ],
	    tasks: ['browserify'],
	    options: {
		spawn: false,
	    },
	},
	connect: {
	    target:{
		options: {
		    port: 9001
		}
	    }
	}
	/*
	  ,
	  bower: {
	  flat: {
	  dest: ‘scripts’,
	  options: {
	  debugging: true
	  }
	  }
	  }
	*/
    });
    grunt.loadNpmTasks('grunt-contrib-connect');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-browserify');
    // grunt.loadNpmTasks(‘main-bower-files’);
    grunt.registerTask(
	'default',
	[ //'bower',
	    'connect',
	    'watch']);
};
