posControllers.controller('EmbalaseCtrl', function ($scope, $location, embalaseService) {
    $scope.embalases = [];
    $scope.addResponse = "";

    embalaseService.getEmbalases()
      .then(
      function (embalases) {
        $scope.embalases = embalases.data;
      }
    );

    $scope.deleteEmbalase = function (embalase) {
      embalaseService.deleteEmbalase(embalase.id)
        .then(
        function (response) {
          if (response.status == 204) {
            var index = $scope.embalases.indexOf(embalase);
            $scope.embalases.splice(index, 1)
          }
        }
      );
    };

  }
);

posControllers.controller('EmbalaseUpdateCtrl', function ($scope, $routeParams, embalaseService) {
    $scope.responseMessage = "";

    if ($routeParams.id != undefined) {
      $scope.title = "Ubah Embalase";
      embalaseService.getEmbalase($routeParams.id)
        .then(function (embalase) {
          $scope.embalase = embalase.data;
        }
      );
    } else {
      $scope.title = "Tambah Embalase";
    }


    $scope.updateEmbalase = function () {
      if ($routeParams.id != undefined) {
        embalaseService.updateEmbalase($scope.embalase)
          .then(function (response) {
            if (response.status == 200) {
              $scope.responseMessage = "Berhasil merubah embalase";
              $scope.alert = "alert alert-success";
            }
          });
      } else {
        embalaseService.addEmbalase($scope.embalase)
          .then(function (response) {
            if (response.status == 201) {
              $scope.responseMessage = "Berhasil menambahkan embalase";
              $scope.alert = "alert alert-success";
            }
          });
      }
    };
  }
);
