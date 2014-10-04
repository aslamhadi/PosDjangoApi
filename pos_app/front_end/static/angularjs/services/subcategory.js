posServices.factory('subCategoryService', ['$http', '$q',
    function ($http, $q) {
        return({
            addSubCategory: addSubCategory,
            getSubCategories: getSubCategories,
            getSubCategory: getSubCategory,
            deleteSubCategory: deleteSubCategory,
            updateSubCategory: updateSubCategory
        });

        function addSubCategory(name) {
            return $http({method: 'POST', url: '/api/subcategories/', data: { name: name }}).
                success(function (data, status, headers, config) {
                    return data;
                }).
                error(function (data, status, headers, config) {
                    console.warn(status);
                });
        }

        function deleteSubCategory(id) {
            return $http({method: 'DELETE', url: '/api/subcategories/' + id + '/'}).
                success(function (data, status, headers, config) {
                    return data;
                }).
                error(function (data, status, headers, config) {
                    console.warn(status);
                });
        }

        function getSubCategories() {
            return $http({method: 'GET', url: '/api/subcategories/'}).
                success(function (data, status, headers, config) {
                    return data;
                }).
                error(function (data, status, headers, config) {
                    console.warn(status);
                });
        }

        function getSubCategory(id) {
            return $http({method: 'GET', url: '/api/subcategories/' + id + '/'}).
                success(function (data, status, headers, config) {
                    return data;
                }).
                error(function (data, status, headers, config) {
                    console.warn(status);
                });
        }

        function updateSubCategory(id, name) {
            return $http({method: 'PUT', url: '/api/subcategories/' + id + '/', data: {name: name}}).
                success(function (data, status, headers, config){
                    return data;
                }).
                error(function (data, status, headers, config){
                   console.warn(status);
                });
        }

    }
]);