posControllers.controller('CategoryCtrl', ['$scope', 'categoryService',
    function ($scope, categoryService) {
        $scope.categories = [];

        loadRemoteData();

        function loadRemoteData() {

            // The categoryService returns a promise.
            categoryService.getCategories()
                .then(
                function (categories) {
                    $scope.categories = categories;
                }
            )
            ;

        }

        $scope.addCategory = function () {
            // If the data we provide is invalid, the promise will be rejected,
            // at which point we can tell the user that something went wrong. In
            // this case, I'm just logging to the console to keep things very
            // simple for the demo.
            categoryService.addCategory($scope.form.name)
                .then(
                loadRemoteData,
                function (errorMessage) {
                    console.warn(errorMessage);
                }
            );

            // Reset the form once values have been consumed.
            $scope.form.name = "";

        };
    }
]);