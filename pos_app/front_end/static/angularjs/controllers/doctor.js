posControllers.controller('DoctorCtrl', function ($scope, $location, doctorService) {
    $scope.doctors = [];
    $scope.title = "Tambah dokter";
    $scope.addResponse = "";
    $scope.doctor = {};
    $scope.doctor.address = "";
    $scope.doctor.city = "";
    $scope.doctor.phone_number = "";

    doctorService.getDoctors()
      .then(
      function (doctors) {
        $scope.doctors = doctors.data;
      }
    );

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
            var index = $scope.doctors.indexOf(doctor);
            $scope.doctors.splice(index, 1)
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
        $scope.doctor.name = doctor.data.user.first_name;
      }
    );

    $scope.updateDoctor = function () {
      doctorService.updateDoctor($scope.doctor)
        .then(function (response) {
          if (response.status == 200) {
            $scope.responseMessage = "Berhasil merubah dokter";
            $scope.alert = "alert alert-success";
          }
        });
    };
  }
);
