posServices.factory('productService', function ($http, $q) {
    return({
      addProduct: addProduct,
      getProducts: getProducts,
      getProduct: getProduct,
      deleteProduct: deleteProduct,
      updateProduct: updateProduct
    });

    function addProduct(product) {
      return $http({method: 'POST', url: '/api/products/', data: {subcategory: product.subcategory.id, unit_type: product.unit_type.id, name: product.name, base_price: product.base_price, sale_price: product.sale_price, tax: product.tax }}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(data);
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

    function updateProduct(product) {
      return $http({method: 'PUT', url: '/api/products/' + product.id + '/', data: { subcategory: product.subcategory.id, unit_type: product.unit_type.id, name: product.name, base_price: product.base_price, sale_price: product.sale_price, tax: product.tax }}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

  }
);
