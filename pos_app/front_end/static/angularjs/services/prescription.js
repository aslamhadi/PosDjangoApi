posServices.factory('prescriptionService', function ($http, $q) {
    return({
      addPrescription: addPrescription
    });

    function addPrescription(data) {
      var url = "/api/prescriptions/create/";
      return $http.post(url, data)
        .success(function (data, status, headers, config) {
          return "berhasil";
        })
        .error(function (data, status, headers, config) {
          console.warn(status);
        });
    }
  }

);
