{% include 'licenses/licenses.php' %}

module.exports = function(grunt) {

	// load needed modules
	grunt.loadNpmTasks('grunt-contrib-concat');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-jshint');
	grunt.loadNpmTasks('grunt-wrap');
	grunt.loadNpmTasks('gruntacular');


	grunt.initConfig({

		meta: {
			pkg: grunt.file.readJSON('package.json'),
			version: '<%= meta.pkg.version %>',
			production: 'public/'
		},

		concat: {
			options: {
				// remove license headers
				stripBanners: true
			},
			dist: {
				src: [
					'config/app.js',
					'config/routes.js',
					'app/controllers/**/*.js',
					'app/directives/**/*.js',
					'app/filters/**/*.js',
					'app/services/**/*.js'
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
					'\n})(window.angular, jQuery);'
				]
			}
		},

		jshint: {
			files: [
				'Gruntfile.js', 
				'app/controllers/**/*.js',
				'app/directives/**/*.js',
				'app/filters/**/*.js',
				'app/services/**/*.js',
				'app/tests/**/*.js', 
				'config/*.js'],
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
					'app/controllers/**/*.js',
					'app/directives/**/*.js',
					'app/filters/**/*.js',
					'app/services/**/*.js',
					'config/*.js'
				],
				tasks: ['build']
			}
		},

		karma: {
			unit: {
				configFile: 'config/karma.js'
			},
			continuous: {
				configFile: 'config/karma.js',
				singleRun: true,
				browsers: ['PhantomJS'],
				reporters: ['progress', 'junit'],
				junitReporter: {
					outputFile: 'test-results.xml'
				}
			}
		}

	});

	// make tasks available under simpler commands
	grunt.registerTask('build', ['jshint', 'concat', 'wrap']);
	grunt.registerTask('watchjs', ['watch:concat']);
	grunt.registerTask('ci', ['testacular:continuous']);
	grunt.registerTask('testjs', ['testacular:unit']);

};