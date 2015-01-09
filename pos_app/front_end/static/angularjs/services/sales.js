posServices.factory('salesService', function ($http, $q) {
    return({
        getSales: getSales,
        getSale: getSale
    });

    function getSales() {
        return $http({method: 'GET', url: '/api/payments/'}).
            success(function (data, status, headers, config) {
                return data;
            }).
            error(function (data, status, headers, config) {
                console.warn(status);
            });
    }

    function getSale(id) {
        return $http({method: 'GET', url: '/api/payments/' + id + '/'}).
            success(function (data, status, headers, config) {
                return data;
            }).
            error(function (data, status, headers, config) {
                console.warn(status);
            });
    }
 }
);
