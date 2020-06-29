module.exports = function(grunt) {
    grunt.initConfig({
        sass: {
            dist: {
                options: {
                    style: 'compressed'
                },
                files: {
                    'static/css/main.css': 'static/css/main.scss'
                }
            }
        },
        watch: {
            sass: {
                files: ['static/css/*.scss'],
                tasks: ['sass:dist']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('default', ['sass:dist']);
};