posControllers.controller('FactoryCtrl', function ($scope, $location, factoryService) {
    $scope.factories = [];
    $scope.addResponse = "";

    getFactories();

    function getFactories() {
      factoryService.getFactories()
        .then(
        function (factories) {
          $scope.factories = factories.data;
        }
      );
    }

    $scope.addFactory = function () {
      factoryService.addFactory($scope.form.name)
        .then(
        function (factory) {
          // The api return data so let's just push the data into factories array
          $scope.factories.push(factory.data);
        }
      );
      // Reset the form once values have been consumed.
      $scope.form.name = "";
    };

    $scope.deleteFactory = function (factory) {
      factoryService.deleteFactory(factory.id)
        .then(
        function (response) {
          if (response.status == 204) {
            var index = $scope.factories.indexOf(factory);
            $scope.factories.splice(index, 1)
          }
        }
      );
    };
  }
);

posControllers.controller('FactoryUpdateCtrl', function ($scope, $routeParams, factoryService) {
    $scope.responseMessage = "";
    getFactory();

    function getFactory() {
      factoryService.getFactory($routeParams.id)
        .then(function (factory) {
          $scope.factory = factory.data;
        }
      );
    }

    $scope.updateFactory = function () {
      factoryService.updateFactory($scope.factory.id, $scope.factory.name)
        .then(function (response) {
          if (response.status == 200) {
            $scope.responseMessage = "Berhasil merubah tipe unit";
            $scope.alert = "alert alert-success";
          }
        });
    };
  }
);
