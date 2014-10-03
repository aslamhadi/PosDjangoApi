'use strict';

/* App modules */

var posAngular = angular.module('posAngular', [
    'ngRoute',
    'ngCookies',
    'posControllers',
    'posServices',
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


// Generate csrf token
posAngular.run( function run( $http, $cookies ){
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});