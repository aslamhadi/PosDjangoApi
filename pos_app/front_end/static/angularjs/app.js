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
                templateUrl: 'static/views/index.html',
                controller: 'HomeCtrl'
            }).
            when('/category/',{
                templateUrl: 'static/views/category/index.html',
                controller: 'CategoryCtrl'
            }).
            otherwise({
               redirectTo: '/'
            });
    }
]);