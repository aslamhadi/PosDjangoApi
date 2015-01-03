posControllers.controller('NewSalesCtrl', function ($scope, $http, $modal, productService, newSaleService) {

  $scope.selected = undefined;
  $scope.products = [];
  $scope.prescriptions = [];
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

    modalInstance.result.then(function (prescription) {
      $scope.prescription.
      $scope.prescriptions.push(prescription);
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
    var data = {
      employee: window.requestUser.id,
      total: $scope.totalPrice,
      cash: $scope.cash,
      change: $scope.change,
      list_product: [],
      list_prescription: []
    };

    angular.forEach($scope.products, function (product) {
      if (product.quantity > 0) {
        data.list_product.push({
          product: product.id,
          item_count: product.quantity,
          discount: product.discount,
          price: product.price
        });
      }
    });

    angular.forEach($scope.prescriptions, function (prescription) {
      data.list_prescription.push({
        prescription: prescription.id,
        item_count: prescription.quantity,
        discount: 0,
        price: prescription.price
      });
    });

    newSaleService.createPayment(data)
      .then(
      function (response) {
        $scope.responseMessage = "Berhasil melakukan penjualan";
        $scope.alert = "alert alert-success";
      }
    );
  }

});


angular.module('posAngular').controller('PrescriptionCtrl',
  function ($scope, $modalInstance, productService, embalaseService, doctorService, prescriptionService) {

    $scope.prescriptions = [];
    $scope.embalases = [];
    $scope.totalPrice = 0;
    $scope.cost_service = 0;

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

    $scope.getProducts = function (name) {
      return productService.searchProductByName(name);
    };

    $scope.getEmbalases = function (name) {
      return embalaseService.searchEmbalaseByName(name);
    };

    // process payment from here
    $scope.updateTotal = function () {
      // set initial total price to 0
      $scope.totalPrice = 0;

      // calculate embalase
      angular.forEach($scope.embalases, function (embalase) {
        embalase.total = embalase.quantity * embalase.price;

        $scope.totalPrice += embalase.total;
        embalase.total = embalase.total.toFixed(2);
      });

      //calculate prescriptions
      angular.forEach($scope.prescriptions, function (prescription) {
        prescription.total = prescription.quantity * prescription.price;

        $scope.totalPrice += prescription.total;
        prescription.total = prescription.total.toFixed(2);
      });
    };

    // get list of doctors
    doctorService.getDoctors()
      .then(
        function(doctors) {
          $scope.doctors = doctors.data;
        }
      );

    function processPayment() {
      console.log($scope.doctor);
      console.log($scope.prescriptions);
      console.log($scope.embalases);

      var data = {
        //employee: window.requestUser.backoffice.user.id,
        sub_total: $scope.totalPrice,
        doctor: $scope.doctor.id,
        cost_service: $scope.cost_service,
        list_product: [],
        list_embalase: []
      };

      angular.forEach($scope.prescriptions, function (prescription) {
        if (prescription.quantity > 0) {
          data.list_product.push({
            product: prescription.id,
            item_count: prescription.quantity,
            price: prescription.price
          });
        }
      });

      angular.forEach($scope.embalases, function (embalase) {
        if (embalase.quantity > 0) {
          data.list_embalase.push({
            embalase: embalase.id,
            item_count: embalase.quantity,
            price: embalase.price
          });
        }
      });

      prescriptionService.addPrescription(data)
        .then(function (response) {
          $modalInstance.close(response.data);
        });
    }

    // process modal
    $scope.ok = function () {
      processPayment();
      //$modalInstance.close();
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  });
