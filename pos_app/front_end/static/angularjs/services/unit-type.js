posServices.factory('unitTypeService', function ($http, $q) {
    return({
      addUnitType: addUnitType,
      getUnitTypes: getUnitTypes,
      getUnitType: getUnitType,
      deleteUnitType: deleteUnitType,
      updateUnitType: updateUnitType
    });

    function addUnitType(name) {
      return $http({method: 'POST', url: '/api/unit-types/', data: { name: name }}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function deleteUnitType(id) {
      return $http({method: 'DELETE', url: '/api/unit-types/' + id + '/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function getUnitTypes() {
      return $http({method: 'GET', url: '/api/unit-types/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function getUnitType(id) {
      return $http({method: 'GET', url: '/api/unit-types/' + id + '/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function updateUnitType(id, name) {
      return $http({method: 'PUT', url: '/api/unit-types/' + id + '/', data: {name: name}}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

  }
);
