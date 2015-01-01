posServices.factory('doctorService', function ($http, $q) {
    return({
      addDoctor: addDoctor,
      getDoctors: getDoctors,
      getDoctor: getDoctor,
      deleteDoctor: deleteDoctor,
      updateDoctor: updateDoctor
    });

    function addDoctor(doctor) {
      return $http({method: 'POST', url: '/api/doctors/', data: {name: doctor.name, price: doctor.price}}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function deleteDoctor(id) {
      return $http({method: 'DELETE', url: '/api/doctors/' + id + '/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function getDoctors() {
      return $http({method: 'GET', url: '/api/doctors/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function getDoctor(id) {
      return $http({method: 'GET', url: '/api/doctors/' + id + '/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function updateDoctor(doctor) {
      return $http({method: 'PUT', url: '/api/doctors/' + doctor.id + '/', data: {name: doctor.name, price: doctor.price}}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }
  }
);
