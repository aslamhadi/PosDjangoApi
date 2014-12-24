posControllers.controller('NewSalesCtrl', function ($scope, $http, productService) {

  $scope.selected = undefined;
  $scope.products = [];
  $scope.totalPrice = 0.00;
  $scope.subTotalPrice = 0.00;

  // callback typeahead
  $scope.onSelect = function ($item, $model, $label) {
    $scope.product = $model;
    $scope.product.total = 0;
    // Set default value in unit type
    $scope.product.unit_type = $scope.product.product_prices[0];

    $scope.products.push($scope.product);

    console.log($model);
  };

  $scope.getProducts = function(name)  {
    return productService.searchProductByName(name);
  };

  $scope.countProductPrice = function() {
    $scope.product.total = $scope.product.unit_type.sale_price * $scope.product.quantity;
  }
});
