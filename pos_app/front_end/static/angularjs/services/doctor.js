posServices.factory('doctorService', function ($http, $q) {
    return({
      addDoctor: addDoctor,
      getDoctors: getDoctors,
      getDoctor: getDoctor,
      deleteDoctor: deleteDoctor,
      updateDoctor: updateDoctor
    });

    function addDoctor(doctor) {
      var username = doctor.name.replace(/ /g,'');
      return $http({method: 'POST', url: '/api/doctors/create/', data: {username: username, first_name: doctor.name, is_staff:false, city: doctor.city, phone_number:doctor.phone_number, address:doctor.address}}).
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
      return $http({method: 'PUT', url: '/api/doctors/' + doctor.id + '/', data: {first_name: doctor.name, city: doctor.city, phone_number:doctor.phone_number, address:doctor.address}}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }
  }
);
