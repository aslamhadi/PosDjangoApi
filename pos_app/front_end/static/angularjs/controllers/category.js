posControllers.controller('CategoryCtrl', function ($scope, $location, categoryService) {
    $scope.categories = [];
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

    $scope.addCategory = function () {
      categoryService.addCategory($scope.form.name)
        .then(
        function (category) {
          // The api return data so let's just push the data into categories array
          $scope.categories.push(category.data);
        }
      );
      // Reset the form once values have been consumed.
      $scope.form.name = "";
    };

    $scope.deleteCategory = function (category) {
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

    $scope.updateCategory = function (categoryId) {
      $location.path('/category/update/' + categoryId + '/');
    };
  }
);

posControllers.controller('CategoryUpdateCtrl', function ($scope, $routeParams, categoryService) {
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
      categoryService.updateCategory($scope.category.id, $scope.category.name)
        .then(function (response) {
          if (response.status == 200) {
            $scope.responseMessage = "Berhasil merubah kategori";
            $scope.alert = "alert alert-success";
          }
        });
    };
  }
);
