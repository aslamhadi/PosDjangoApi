posControllers.controller('NewSalesCtrl', function ($scope, $http, productService) {

  $scope.selected = undefined;
  $scope.products = [];

  // callback typeahead
  $scope.onSelect = function ($item, $model, $label) {
    $scope.product = $model;
    $scope.products.push($scope.product);
    console.log($model);
    // console.log($item);
    // console.log($label);
  };

  $scope.getProducts = function(name)  {
    return productService.searchProductByName(name);
  }
});
