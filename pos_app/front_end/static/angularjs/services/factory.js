posServices.factory('factoryService', function ($http, $q) {
    return({
      addFactory: addFactory,
      getFactories: getFactories,
      getFactory: getFactory,
      deleteFactory: deleteFactory,
      updateFactory: updateFactory
    });

    function addFactory(name) {
      return $http({method: 'POST', url: '/api/factories/', data: { name: name }}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function deleteFactory(id) {
      return $http({method: 'DELETE', url: '/api/factories/' + id + '/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function getFactories() {
      return $http({method: 'GET', url: '/api/factories/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function getFactory(id) {
      return $http({method: 'GET', url: '/api/factories/' + id + '/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function updateFactory(id, name) {
      return $http({method: 'PUT', url: '/api/factories/' + id + '/', data: {name: name}}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

  }
);
