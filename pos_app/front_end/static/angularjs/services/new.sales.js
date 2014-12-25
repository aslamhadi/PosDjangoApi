posServices.factory('newSaleService', function ($http, $q) {
    return({
      createPayment: createPayment
    });

    function createPayment(data) {
      var url = "/api/payments/create/";
      $http.post(url, data)
      .success(function (data, status, headers, config) {
        return "berhasil";
      })
      .error(function (data, status, headers, config) {
        console.warn(status);
      });
    }
  }

);
