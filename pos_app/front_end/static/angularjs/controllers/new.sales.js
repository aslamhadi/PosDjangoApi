posControllers.controller('NewSalesCtrl', function ($scope, $http, productService) {
  $scope.onSelect = function ($item, $model, $label) {
    $scope.$item = $item;
    $scope.$model = $model;
    $scope.$label = $label;
    console.log($item);
    console.log($model);
    console.log($label);
  };
  $scope.selected = undefined;

  $scope.products = [];

  productService.getProducts()
    .then(
    function (products) {
      $scope.all_products = products.data;
    }
  );
});
