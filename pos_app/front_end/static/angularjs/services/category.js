var posServices = angular.module('posServices', []);

posServices.factory('categoryService', function ($http, $q) {
    return({
      addCategory: addCategory,
      getCategories: getCategories,
      getCategory: getCategory,
      deleteCategory: deleteCategory,
      updateCategory: updateCategory
    });

    function addCategory(category) {
      return $http({method: 'POST', url: '/api/categories/', data: { name: category.name, idx_sale_price: category.idx_sale_price, idx_sale_price_prescription: category.idx_sale_price_prescription  }}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function deleteCategory(id) {
      return $http({method: 'DELETE', url: '/api/categories/' + id + '/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function getCategories() {
      return $http({method: 'GET', url: '/api/categories/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function getCategory(id) {
      return $http({method: 'GET', url: '/api/categories/' + id + '/'}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

    function updateCategory(id, category) {
      return $http({method: 'PUT', url: '/api/categories/' + id + '/', data: { name: category.name, idx_sale_price: category.idx_sale_price, idx_sale_price_prescription: category.idx_sale_price_prescription  }}).
        success(function (data, status, headers, config) {
          return data;
        }).
        error(function (data, status, headers, config) {
          console.warn(status);
        });
    }

  }
);
