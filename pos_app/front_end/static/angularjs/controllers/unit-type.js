posControllers.controller('UnitTypeCtrl', ['$scope', '$location', 'unitTypeService',
    function ($scope, $location, unitTypeService) {
        $scope.unitTypes = [];
        $scope.addResponse = "";

        getUnitTypes();

        function getUnitTypes() {
            unitTypeService.getUnitTypes()
                .then(
                function (unitTypes) {
                    $scope.unitTypes = unitTypes.data;
                }
            );
        }

        $scope.addUnitType = function () {
            unitTypeService.addUnitType($scope.form.name)
                .then(
                function (unitType) {
                    // The api return data so let's just push the data into unitTypes array
                    $scope.unitTypes.push(unitType.data);
                }
            );
            // Reset the form once values have been consumed.
            $scope.form.name = "";
        };

        $scope.deleteUnitType = function (unitType) {
            unitTypeService.deleteUnitType(unitType.id)
                .then(
                function (response) {
                    if (response.status == 204) {
                        var index = $scope.unitTypes.indexOf(unitType);
                        $scope.unitTypes.splice(index, 1)
                    }
                }
            );
        };

        $scope.updateUnitType = function (unitTypeId) {
            $location.path('/unitType/update/' + unitTypeId);
        };
    }
]);

posControllers.controller('UnitTypeUpdateCtrl', ['$scope', '$routeParams', 'unitTypeService',
    function($scope, $routeParams, unitTypeService) {
        $scope.responseMessage = "";
        getUnitType();

        function getUnitType() {
            unitTypeService.getUnitType($routeParams.id)
                .then(function (unitType) {
                    $scope.unitType = unitType.data;
                }
            );
        }

        $scope.updateUnitType = function () {
            unitTypeService.updateUnitType($scope.unitType.id, $scope.unitType.name)
                .then(function(response){
                    if (response.status == 200) $scope.responseMessage = "Berhasil merubah tipe unit";
                });
        };
    }
]);