'use strict';

/* App modules */

var posAngular = angular.module('posAngular', [
  'ngRoute',
  'ngCookies',
  'posControllers',
  'posServices',
]);

posAngular.config(['$routeProvider',
  function ($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'static/angularjs/views/index.html',
        controller: 'HomeCtrl'
      }).
      when('/category/', {
        templateUrl: 'static/angularjs/views/category/index.html',
        controller: 'CategoryCtrl'
      }).
      when('/category/update/:id/', {
        templateUrl: 'static/angularjs/views/category/update.html',
        controller: 'CategoryUpdateCtrl'
      }).
      when('/subcategory/', {
        templateUrl: 'static/angularjs/views/subcategory/index.html',
        controller: 'SubCategoryCtrl'
      }).
      when('/subcategory/update/:id/', {
        templateUrl: 'static/angularjs/views/subcategory/update.html',
        controller: 'SubCategoryUpdateCtrl'
      }).
      when('/unit-type/', {
        templateUrl: 'static/angularjs/views/unit-type/index.html',
        controller: 'UnitTypeCtrl'
      }).
      when('/unit-type/update/:id/', {
        templateUrl: 'static/angularjs/views/unit-type/update.html',
        controller: 'UnitTypeUpdateCtrl'
      }).
      when('/product/', {
        templateUrl: 'static/angularjs/views/product/index.html',
        controller: 'ProductCtrl'
      }).
      when('/product/add/', {
        templateUrl: 'static/angularjs/views/product/update.html',
        controller: 'ProductUpdateCtrl'
      }).
      when('/product/update/:id/', {
        templateUrl: 'static/angularjs/views/product/update.html',
        controller: 'ProductUpdateCtrl'
      }).
      when('/sales/new/', {
        templateUrl: 'static/angularjs/views/sales/new.html',
        controller: 'NewSalesCtrl'
      }).
      otherwise({
        redirectTo: '/'
      });
  }
]);


// Generate csrf token
posAngular.run(function run($http, $cookies) {
  $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});
