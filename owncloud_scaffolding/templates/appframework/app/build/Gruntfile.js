{% include 'licenses/licenses.php' %}

module.exports = function(grunt) {

	// load needed modules
	grunt.loadNpmTasks('grunt-contrib-concat');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-jshint');
	grunt.loadNpmTasks('grunt-wrap');
	grunt.loadNpmTasks('grunt-karma');
	grunt.loadNpmTasks('grunt-phpunit');


	grunt.initConfig({

		meta: {
			pkg: grunt.file.readJSON('package.json'),
			version: '<%= meta.pkg.version %>',
			production: '../js/public/'
		},

		concat: {
			options: {
				// remove license headers
				stripBanners: true
			},
			dist: {
				src: [
					'../js/config/app.js',
					'../js/app/**/*.js'
				],
				dest: '<%= meta.production %>app.js'
			}
		},

		wrap: {
			app: {
				src: ['<%= meta.production %>app.js'],
				dest: '',
				wrapper: [
					'(function(angular, $, undefined){\n\n\'use strict\';\n\n',
					'\n})(angular, jQuery);'
				]
			}
		},

		jshint: {
			files: [
				'Gruntfile.js',
				'../js/app/**/*.js',
				'../js/config/*.js',
				'../tests/js/unit/**/*.js'
			],
			options: {
				// options here to override JSHint defaults
				globals: {
					console: true
				}
			}
		},

		watch: {
			// this watches for changes in the app directory and runs the concat
			// and wrap tasks if something changed
			concat: {
				files: [
					'../js/app/**/*.js',
					'../js/config/*.js'
				],
				tasks: ['build']
			},
			phpunit: {
				files: '../**/*.php',
				tasks: ['phpunit']
			}
		},

		phpunit: {
			classes: {
				dir: '../tests/php/unit'
			},
			options: {
				colors: true
			}
		},

		karma: {
			unit: {
				configFile: '../tests/js/config/karma.js'
			},
			continuous: {
				configFile: '../tests/js/config/karma.js',
				singleRun: true,
				browsers: ['PhantomJS'],
				reporters: ['progress', 'junit'],
				junitReporter: {
					outputFile: '../tests/js/test-results.xml'
				}
			}
		}

	});

	// make tasks available under simpler commands
	grunt.registerTask('build', ['jshint', 'concat', 'wrap']);

};
