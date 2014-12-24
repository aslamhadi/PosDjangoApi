var posControllers = angular.module('posControllers', []);

posControllers.controller('HomeCtrl', function ($scope) {
    $scope.batman = window.requestUser.username;
  }
);
