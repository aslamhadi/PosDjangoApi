posServices.factory('productService', ['$http', '$q',
  function ($http, $q) {
    return({
      addProduct: addProduct,
      getProducts: getProducts,
      getProduct: getProduct,
      deleteProduct: deleteProduct,
      updateProduct: updateProduct
    });

    function addProduct(name, product) {
      return $http({method: 'POST', url: '/api/products/', data: {product: product, name: name }}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function deleteProduct(id) {
      return $http({method: 'DELETE', url: '/api/products/' + id + '/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function getProducts() {
      return $http({method: 'GET', url: '/api/products/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function getProduct(id) {
      return $http({method: 'GET', url: '/api/products/' + id + '/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function updateProduct(id, name, product) {
      return $http({method: 'PUT', url: '/api/products/' + id + '/', data: {product: product, name: name }}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

  }
]);