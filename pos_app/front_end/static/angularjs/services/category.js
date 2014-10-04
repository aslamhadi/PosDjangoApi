var posServices = angular.module('posServices', []);

posServices.factory('categoryService', ['$http', '$q',
    function ($http, $q) {
        return({
            addCategory: addCategory,
            getCategories: getCategories,
            deleteCategory: deleteCategory
        });

        function addCategory(name) {
            return $http({method: 'POST', url: '/api/categories/', data: { name: name }}).
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
    }
]);