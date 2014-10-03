var posControllers = angular.module('posControllers', []);

posControllers.controller('HomeCtrl', ['$scope',
    function($scope) {
        $scope.batman = "batmaaan";
    }
]);