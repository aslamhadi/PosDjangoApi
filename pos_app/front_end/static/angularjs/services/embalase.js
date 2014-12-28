posServices.factory('embalaseService', function ($http, $q) {
    return({
      addEmbalase: addEmbalase,
      getEmbalases: getEmbalases,
      getEmbalase: getEmbalase,
      deleteEmbalase: deleteEmbalase,
      updateEmbalase: updateEmbalase
    });

    function addEmbalase(embalase) {
      return $http({method: 'POST', url: '/api/embalases/', data: {name: embalase.name, price: embalase.price}}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function deleteEmbalase(id) {
      return $http({method: 'DELETE', url: '/api/embalases/' + id + '/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function getEmbalases() {
      return $http({method: 'GET', url: '/api/embalases/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function getEmbalase(id) {
      return $http({method: 'GET', url: '/api/embalases/' + id + '/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function updateEmbalase(embalase) {
      return $http({method: 'PUT', url: '/api/embalases/' + embalase.id + '/', data: {name: embalase.name, price: embalase.price}}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

  }
);
