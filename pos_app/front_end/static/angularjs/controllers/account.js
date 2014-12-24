posControllers.controller('AccountCtrl', function ($scope, $http, $location) {
  $http.post('/api/logout/').
    success(function(data, status, headers, config) {
      $location.path('/');
      window.location.reload();
    }).
    error(function(data, status, headers, config) {
      console.log(status);
    });
});
