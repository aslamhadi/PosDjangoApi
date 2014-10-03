'use strict';

/* App modules */

var posAngular = angular.module('posAngular', [
    'ngRoute',
    'posControllers'
]);

posAngular.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: 'templates/index.html',
                controller: 'HomeCtrl'
            }).
            otherwise({
               redirectTo: '/'
            });
    }
]);