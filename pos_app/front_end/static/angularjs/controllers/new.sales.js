posControllers.controller('NewSalesCtrl', function ($scope, $http, $modal, productService, newSaleService) {

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

  $scope.getProducts = function (name) {
    return productService.searchProductByName(name);
  };

  $scope.updateChange = function () {
    $scope.change = $scope.cash - $scope.totalPrice;
  };

  $scope.removeProduct = function (index) {
    $scope.products.splice(index, 1);
  };

  $scope.openModal = function (size) {

    var modalInstance = $modal.open({
      templateUrl: 'modalPrescription.html',
      controller: 'PrescriptionCtrl',
      size: size
//      resolve: {
//        items: function () {
//          return $scope.items;
//        }
//      }
    });

    modalInstance.result.then(function (selectedItem) {
      $scope.selected = selectedItem;
    });
  };

  $scope.createPayment = function () {
    if ($scope.totalPrice == 0) {
      $scope.errorMessage = "Belum ada produk";
    } else if ($scope.cash == 0) {
      $scope.errorMessage = "Silakan masukkan jumlah uang";
    } else {
      processPayment();
    }
  };


  // process payment from here
  $scope.updateTotal = function () {
    $scope.totalPrice = 0;
    angular.forEach($scope.products, function (product) {
      var disc = product.discount * product.price / 100;

      product.total = product.quantity * product.price;
      product.total -= disc;

      $scope.totalPrice += product.total;
      product.total = product.total.toFixed(2);
    });
  };

  function processPayment() {
    $scope.errorMessage = "";
    $scope.checkoutButton = "Memproses...";
    // process payment here
    data = {
      employee: window.requestUser.backoffice.user.id,
      total: $scope.totalPrice,
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
          price: product.price
        });
      }
    });

    newSaleService.createPayment(data);
  };

});


angular.module('posAngular').controller('PrescriptionCtrl',
  function ($scope, $modalInstance, productService, embalaseService, doctorService) {

    $scope.prescriptions = [];
    $scope.embalases = [];
    $scope.totalPrice = 0;

    // callback typeahead
    $scope.onSelectPrescription = function ($item, $model, $productel) {
      $scope.prescription = $model;
      $scope.prescription.total = 0;
      $scope.prescription.quantity = 1;
      $scope.prescription.discount = 0;

      $scope.prescriptions.push($scope.prescription);
      $scope.updateTotal();

      console.log($model);
    };

    $scope.onSelectEmbalase = function ($item, $model, $productel) {
      $scope.embalase = $model;
      $scope.embalase.total = 0;
      $scope.embalase.quantity = 1;
      $scope.embalase.discount = 0;

      $scope.embalases.push($scope.embalase);
      $scope.updateTotal();

      console.log($model);
    };

    $scope.getEmbalases = function (name) {
      return embalaseService.searchEmbalaseByName(name);
    };

    // process payment from here
    $scope.updateTotal = function () {
      $scope.totalPrice = 0;
      angular.forEach($scope.products, function (product) {
        var disc = product.discount * product.price / 100;

        product.total = product.quantity * product.price;
        product.total -= disc;

        $scope.totalPrice += product.total;
        product.total = product.total.toFixed(2);
      });
    };

    // get list of doctors
    doctorService.getDoctors()
      .then(
        function(doctors) {
          $scope.doctors = doctors.data;
        }
      );

    // process modal
    $scope.ok = function () {
      $modalInstance.close();
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  });
