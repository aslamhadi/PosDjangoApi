posControllers.controller('ProductCtrl', ['$scope', '$location', 'productService',
  function ($scope, $location, productService) {
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
]);

posControllers.controller('ProductUpdateCtrl', ['$scope', '$routeParams', 'productService', 'categoryService', 'subCategoryService', 'unitTypeService',
  function ($scope, $routeParams, productService, categoryService, subCategoryService, unitTypeService) {
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
      if ($scope.product != null) {
        productService.updateProduct($scope.product.id, $scope.product.name)
          .then(function (response) {
            if (response.status == 200) {
              $scope.responseMessage = "Berhasil merubah produk";
              $scope.alert = "alert alert-success";
            }
          });
      } else {
        productService.addProduct($scope.subcategory.id, $scope.unit_type.id, $scope.name, $scope.base_price, $scope.sale_price, $scope.tax)
          .then(function (response) {
            if (response.status == 201) {
              $scope.responseMessage = "Berhasil menambah produk";
              $scope.alert = "alert alert-success";
            }
          });
      }
    };
  }
]);