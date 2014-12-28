posControllers.controller('NewSalesCtrl', function ($scope, $http, productService, newSaleService) {

  $scope.selected = undefined;
  $scope.products = [];
  $scope.totalPrice = 0;
  $scope.cash = 0;
  $scope.change = 0;
  $scope.errorMessage = "";
  $scope.checkoutButton = "Bayar";

  // callback typeahead
  $scope.onSelect = function ($item, $model, $productel) {
    $scope.product = $model;
    $scope.product.total = 0;
    $scope.product.quantity = 1;
    $scope.product.discount = 0;
    $scope.product.is_prescription = false;

    $scope.products.push($scope.product);
    $scope.updateTotal();

    console.log($model);
  };

  $scope.getProducts = function(name)  {
    return productService.searchProductByName(name);
  };

  $scope.updateTotal = function () {
    $scope.totalPrice = 0;
    angular.forEach($scope.products, function (product) {
      var disc = product.discount * product.price / 100;

      product.total = product.quantity * product.price;
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

  $scope.createPayment = function() {
    if ($scope.totalPrice == 0) {
      $scope.errorMessage = "Belum ada produk";
    } else if ($scope.cash == 0) {
      $scope.errorMessage = "Silakan masukkan jumlah uang";
    } else {
      processPayment();
    }
  };

  function processPayment() {
    $scope.errorMessage = "";
    $scope.checkoutButton = "Memproses...";
    // process payment here
    data = {
      employee: window.requestUser.backoffice.user.id,
      total : $scope.totalPrice,
      list_product: []
    };

    angular.forEach($scope.labs, function (product) {
      if (product.license > 0) {
        data.list_product.push({
          product: product.id,
          item_count: product.quantity,
          is_prescription: product.is_prescription,
          idx_sale_price: product.idx_sale_price,
          discount: product.discount,
          price: product.price,
        });
      }
    });

    newSaleService.createPayment(data);
  };

});
