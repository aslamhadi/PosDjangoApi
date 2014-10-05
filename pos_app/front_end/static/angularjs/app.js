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
            when('/category/update/:id',{
                templateUrl: 'static/views/category/update.html',
                controller: 'CategoryUpdateCtrl'
            }).
            when('/subcategory/',{
                templateUrl: 'static/views/subcategory/index.html',
                controller: 'SubCategoryCtrl'
            }).
            when('/subcategory/update/:id',{
                templateUrl: 'static/views/subcategory/update.html',
                controller: 'SubCategoryUpdateCtrl'
            }).
            when('/unit-type/',{
                templateUrl: 'static/views/unit-type/index.html',
                controller: 'UnitTypeCtrl'
            }).
            when('/category/update/:id',{
                templateUrl: 'static/views/unit-type/update.html',
                controller: 'UnitTypeUpdateCtrl'
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