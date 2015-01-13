'use strict';

/* App modules */

var posAngular = angular.module('posAngular', [
  'ngRoute',
  'ngCookies',
  'ui.bootstrap',
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
      when('/logout', {
        template: ' ',
        controller: 'AccountCtrl'
      }).
      when('/category/', {
        templateUrl: 'static/angularjs/views/category/index.html',
        controller: 'CategoryCtrl'
      }).
      when('/category/add/', {
        templateUrl: 'static/angularjs/views/category/update.html',
        controller: 'CategoryCtrl'
      }).
      when('/category/update/:id/', {
        templateUrl: 'static/angularjs/views/category/update.html',
        controller: 'CategoryUpdateCtrl'
      }).
      when('/doctor/', {
        templateUrl: 'static/angularjs/views/doctor/index.html',
        controller: 'DoctorCtrl'
      }).
      when('/doctor/add/', {
        templateUrl: 'static/angularjs/views/doctor/update.html',
        controller: 'DoctorCtrl'
      }).
      when('/doctor/update/:id/', {
        templateUrl: 'static/angularjs/views/doctor/update.html',
        controller: 'DoctorUpdateCtrl'
      }).
      when('/embalase/', {
        templateUrl: 'static/angularjs/views/embalase/index.html',
        controller: 'EmbalaseCtrl'
      }).
      when('/embalase/add/', {
        templateUrl: 'static/angularjs/views/embalase/update.html',
        controller: 'EmbalaseUpdateCtrl'
      }).
      when('/embalase/update/:id/', {
        templateUrl: 'static/angularjs/views/embalase/update.html',
        controller: 'EmbalaseUpdateCtrl'
      }).
      when('/factory/', {
        templateUrl: 'static/angularjs/views/factory/index.html',
        controller: 'FactoryCtrl'
      }).
      when('/factory/update/:id/', {
        templateUrl: 'static/angularjs/views/factory/update.html',
        controller: 'FactoryUpdateCtrl'
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
      when('/sales/', {
        templateUrl: 'static/angularjs/views/sales/index.html',
        controller: 'SalesCtrl'
      }).
      when('/sales/detail/:id', {
        templateUrl: 'static/angularjs/views/sales/details.html',
        controller: 'SalesDetailCtrl'
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
