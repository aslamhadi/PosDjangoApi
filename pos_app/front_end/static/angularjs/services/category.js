var posServices = angular.module('posServices', []);

posServices.factory('categoryService', ['$http', '$q',
    function ($http, $q) {

        return({
            addCategory: addCategory,
            getCategories: getCategories
            //removeCategory: removeCategory
        });

        function addCategory(name) {

            var request = $http({
                method: "POST",
                url: "/api/categories/",
                data: {
                    name: name
                }
            });

            return( request.then(handleSuccess, handleError) );

        }

        function getCategories() {
            var request = $http({
                method: "GET",
                url: "/api/categories/"
                //headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            });

            return( request.then(handleSuccess, handleError) );
        }

        function handleError(response) {

            // The API response from the server should be returned in a
            // nomralized format. However, if the request was not handled by the
            // server (or what not handles properly - ex. server error), then we
            // may have to normalize it on our end, as best we can.
            if (
                !angular.isObject(response.data) || !response.data.message
                ) {

                return( $q.reject("An unknown error occurred.") );

            }

            // Otherwise, use expected error message.
            return( $q.reject(response.data.message) );

        }


        // I transform the successful response, unwrapping the application data
        // from the API response payload.
        function handleSuccess(response) {

            return( response.data );

        }
    }
]);


//        $http({method: 'GET', url: '/api/categories'}).
//            success(function (data, status, headers, config) {
//                return data;
//            }).
//            error(function (data, status, headers, config) {
//                console.log(status);
//            });