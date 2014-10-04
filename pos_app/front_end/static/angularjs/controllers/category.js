posControllers.controller('CategoryCtrl', ['$scope', 'categoryService',
    function ($scope, categoryService) {
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
    }
]);