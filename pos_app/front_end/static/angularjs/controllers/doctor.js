posControllers.controller('DoctorCtrl', function ($scope, $location, doctorService) {
    $scope.categories = [];
    $scope.title = "Tambah dokter";
    $scope.addResponse = "";

    getDoctors();

    function getDoctors() {
      doctorService.getDoctors()
        .then(
        function (categories) {
          $scope.categories = categories.data;
        }
      );
    }

    $scope.updateDoctor = function () {
      doctorService.addDoctor($scope.doctor)
        .then(
        function (doctor) {
          $scope.responseMessage = "Berhasil menambah dokter";
          $scope.alert = "alert alert-success";
        }
      );
    };

    $scope.deleteDoctor = function (doctor) {
      doctorService.deleteDoctor(doctor.id)
        .then(
        function (response) {
          if (response.status == 204) {
            var index = $scope.categories.indexOf(doctor);
            $scope.categories.splice(index, 1)
          }
        }
      );
    };
  }
);

posControllers.controller('DoctorUpdateCtrl', function ($scope, $routeParams, doctorService) {
    $scope.title = "Update dokter";
    $scope.responseMessage = "";

    doctorService.getDoctor($routeParams.id)
      .then(function (doctor) {
        $scope.doctor = doctor.data;
      }
    );

    $scope.updateDoctor = function () {
      doctorService.updateDoctor($scope.doctor.id, $scope.doctor)
        .then(function (response) {
          if (response.status == 200) {
            $scope.responseMessage = "Berhasil merubah dokter";
            $scope.alert = "alert alert-success";
          }
        });
    };
  }
);
