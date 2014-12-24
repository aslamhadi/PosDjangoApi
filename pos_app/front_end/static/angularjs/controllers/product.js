posControllers.controller('ProductCtrl', function ($scope, $location, productService) {
    $scope.products = [];
    $scope.addResponse = "";

    getProducts();

    function getProducts() {
      productService.getProducts()
        .then(
        function (products) {
          $scope.products = products.data;
        }
      );
    }

    $scope.addProduct = function () {
      productService.addProduct($scope.form.name)
        .then(
        function (product) {
          // The api return data so let's just push the data into products array
          $scope.products.push(product.data);
        }
      );
      // Reset the form once values have been consumed.
      $scope.form.name = "";
    };

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

    $scope.updateProduct = function (productId) {
      $location.path('/product/update/' + productId + '/');
    };
  }
);

posControllers.controller('ProductUpdateCtrl', function ($scope, $routeParams, productService, categoryService, subCategoryService, unitTypeService) {
    $scope.responseMessage = "";
    getProduct();
    getCategories();
    getUnitTypes();

    function getUnitTypes() {
      unitTypeService.getUnitTypes()
        .then(function (unit_types) {
          $scope.unit_types = unit_types.data;
        }
      );
    }

    function getProduct() {
      if ($routeParams.id != undefined) {
        productService.getProduct($routeParams.id)
          .then(function (product) {
            $scope.product = product.data;
          }
        );
      }
    }

    function getCategories() {
      categoryService.getCategories()
        .then(function (categories) {
          $scope.categories = categories.data;
        }
      );
    }

    $scope.getSubcategories = function (category) {
      if (category != null) {
        subCategoryService.getSubCategoriesInCategory(category)
          .then(function (subcategories) {
            $scope.subcategories = subcategories.data;
          }
        )
      }
    };

    $scope.updateProduct = function () {
      var product_prices = [];
        product_prices.push({
          unit_type: $scope.product.unit_type.id,
          sale_price: $scope.product.sale_price,
        });
      if ($routeParams.id != undefined) {
        productService.updateProduct($scope.product, product_prices)
          .then(function (response) {
            if (response.status == 200) {
              $scope.responseMessage = "Berhasil merubah produk";
              $scope.alert = "alert alert-success";
            }
          });
      } else {
        productService.addProduct($scope.product, product_prices)
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
