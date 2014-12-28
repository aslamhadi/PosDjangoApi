posControllers.controller('CategoryCtrl', function ($scope, $location, categoryService) {
    $scope.categories = [];
    $scope.title = "Tambah kategori obat"
    $scope.addResponse = "";

    getCategories();

    function getCategories() {
      categoryService.getCategories()
        .then(
        function (categories) {
          $scope.categories = categories.data;
        }
      );
    }

    $scope.updateCategory = function () {
      categoryService.addCategory($scope.category)
        .then(
        function (category) {
          $scope.responseMessage = "Berhasil menambah kategori";
          $scope.alert = "alert alert-success";
        }
      );
    };

    $scope.deleteCategoryLink = function (category) {
      categoryService.deleteCategory(category.id)
        .then(
        function (response) {
          if (response.status == 204) {
            var index = $scope.categories.indexOf(category);
            $scope.categories.splice(index, 1)
          }
        }
      );
    };

    $scope.updateCategoryLink = function (categoryId) {
      $location.path('/category/update/' + categoryId + '/');
    };
  }
);

posControllers.controller('CategoryUpdateCtrl', function ($scope, $routeParams, categoryService) {
    $scope.title = "Update kategori obat";
    $scope.responseMessage = "";
    getCategory();

    function getCategory() {
      categoryService.getCategory($routeParams.id)
        .then(function (category) {
          $scope.category = category.data;
        }
      );
    }

    $scope.updateCategory = function () {
      categoryService.updateCategory($scope.category.id, $scope.category)
        .then(function (response) {
          if (response.status == 200) {
            $scope.responseMessage = "Berhasil merubah kategori";
            $scope.alert = "alert alert-success";
          }
        });
    };
  }
);
