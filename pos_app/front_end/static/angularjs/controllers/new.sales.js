posControllers.controller('NewSalesCtrl', function ($scope, $http, productService) {

  $scope.selected = undefined;
  $scope.products = [];
  $scope.totalPrice = 0;
  $scope.cash = 0;
  $scope.change = 0;

  // callback typeahead
  $scope.onSelect = function ($item, $model, $productel) {
    $scope.product = $model;
    $scope.product.total = 0;
    $scope.product.quantity = 0;
    $scope.product.discount = 0;
    // Set default value in unit type
    $scope.product.unit_type = $scope.product.product_prices[0];

    $scope.products.push($scope.product);

    console.log($model);
  };

  $scope.getProducts = function(name)  {
    return productService.searchProductByName(name);
  };

  $scope.updateTotal = function () {
    $scope.totalPrice = 0;
    angular.forEach($scope.products, function (product) {
      var disc = product.discount * product.unit_type.price / 100;

      product.total = product.quantity * product.unit_type.price;
      product.total-= disc;

      $scope.totalPrice += product.total;
      product.total = product.total.toFixed(2);
    });
  };

  $scope.updateChange = function () {
    $scope.change = $scope.cash - $scope.totalPrice;
  };

  $scope.removeProduct = function(index) {
    $scope.products.splice(index, 1);
  };
});
