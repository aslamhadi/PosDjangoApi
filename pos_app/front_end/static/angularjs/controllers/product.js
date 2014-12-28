posControllers.controller('ProductCtrl', function ($scope, $location, productService) {
    $scope.products = [];
    $scope.addResponse = "";

    productService.getProducts()
      .then(
      function (products) {
        $scope.products = products.data;
      }
    );

    $scope.deleteProduct = function (product) {
      productService.deleteProduct(product.id)
        .then(
        function (response) {
          if (response.status == 204) {
            var index = $scope.products.indexOf(product);
            $scope.products.splice(index, 1)
          }
        }
      );
    };
  }
);

posControllers.controller('ProductUpdateCtrl', function ($scope, $routeParams, productService, categoryService, factoryService, unitTypeService) {
    $scope.responseMessage = "";
    if ($routeParams.id != undefined) {
      $scope.title = "Update produk";
      productService.getProduct($routeParams.id)
        .then(function (product) {
          $scope.product = product.data;
        }
      );
    } else {
      $scope.title = "Tambah produk";
    }

    unitTypeService.getUnitTypes()
      .then(function (unit_types) {
        $scope.unit_types = unit_types.data;
        $scope.unit_type = $scope.unit_types[0];
      }
    );

    categoryService.getCategories()
      .then(function (categories) {
        $scope.categories = categories.data;
        $scope.category = $scope.categories[0];
      }
    );

    factoryService.getFactories()
      .then(function (factories) {
        $scope.factories = factories.data;
        $scope.factory = $scope.factories[0];
      }
    );

    $scope.updateProduct = function () {
      if ($routeParams.id != undefined) {
        productService.updateProduct($scope.product, $scope.category, $scope.unit_type, $scope.factory)
          .then(function (response) {
            if (response.status == 200) {
              $scope.responseMessage = "Berhasil merubah produk";
              $scope.alert = "alert alert-success";
            }
          });
      } else {
        productService.addProduct($scope.product, $scope.category, $scope.unit_type, $scope.factory)
          .then(function (response) {
            if (response.status == 201) {
              $scope.responseMessage = "Berhasil menambah produk";
              $scope.alert = "alert alert-success";
            }
          });
      }
    };
  }
);
