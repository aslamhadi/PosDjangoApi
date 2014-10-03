posControllers.controller('CategoryCtrl', ['$scope', 'categoryService',
    function ($scope, categoryService) {
        $scope.categories = [];

        getCategories();

        function getCategories() {
            // The categoryService returns a promise.
            categoryService.getCategories()
                .then(
                function (categories) {
                    $scope.categories = categories;
                }
            );
        }

        $scope.addCategory = function () {
            categoryService.addCategory($scope.form.name)
                .then(
                function (category) {
                    // The api return data so let's just push the data into categories array
                    $scope.categories.push(category);
                },
                function (errorMessage) {
                    // Add warning if something unpleasant happens
                    console.warn(errorMessage);
                }
            );

            // Reset the form once values have been consumed.
            $scope.form.name = "";

        };
    }
]);