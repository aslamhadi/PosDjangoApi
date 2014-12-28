posServices.factory('productService', function ($http, $q) {
  return({
    addProduct: addProduct,
    getProducts: getProducts,
    getProduct: getProduct,
    deleteProduct: deleteProduct,
    updateProduct: updateProduct,
    searchProductByName: searchProductByName,
  });

  function addProduct(product, category, unit_type, factory) {
    return $http({method: 'POST', url: '/api/products/create/', data: { category: category.id, unit_type: unit_type.id, factory: factory.id, name: product.name, barcode: product.barcode, price: product.price }}).
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

  function updateProduct(product, product_prices) {
    return $http({method: 'PUT', url: '/api/products/' + product.id + '/', data: { categories: product.categories, name: product.name, product_prices: product_prices }}).
    success(function (data, status, headers, config) {
      return data;
    }).
    error(function (data, status, headers, config) {
      console.warn(status);
    });
  }

  function searchProductByName(name) {
    return $http.get('/api/products/name/' + name + '/')
    .then(function (response) {
      return response.data;
    });
  }
}
);
