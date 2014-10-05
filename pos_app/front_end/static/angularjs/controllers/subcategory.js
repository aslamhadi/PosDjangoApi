posControllers.controller('SubCategoryCtrl', ['$scope', '$location', 'categoryService', 'subCategoryService',
    function ($scope, $location, categoryService, subCategoryService) {
        $scope.subcategories = [];
        $scope.categories = [];
        $scope.addResponse = "";
        $scope.subCategoryName = "";

        getCategories();

        function getCategories() {
            categoryService.getCategories()
                .then(
                function (categories) {
                    $scope.categories = categories.data;
                    $scope.category = categories.data[0];
                }
            );
        }

        getSubCategories();

        function getSubCategories() {
            subCategoryService.getSubCategories()
                .then(
                function (subcategories) {
                    $scope.subcategories = subcategories.data;
                }
            );
        }

        $scope.addSubCategory = function () {
            subCategoryService.addSubCategory($scope.subCategoryName, $scope.category.id)
                .then(
                function (subcategory) {
                    // The api return data so let's just push the data into subcategories array
                    $scope.subcategories.push(subcategory.data);
                }
            );
            // Reset the form once values have been consumed.
            $scope.subCategoryName = "";
        };

        $scope.deleteSubCategory = function (subcategory) {
            subCategoryService.deleteSubCategory(subcategory.id)
                .then(
                function (response) {
                    if (response.status == 204) {
                        var index = $scope.subcategories.indexOf(subcategory);
                        $scope.subcategories.splice(index, 1)
                    }
                }
            );
        };

        $scope.updateSubCategory = function (subcategoryId) {
            $location.path('/subcategory/update/' + subcategoryId);
        };
    }
]);

posControllers.controller('SubCategoryUpdateCtrl', ['$scope', '$routeParams', 'subCategoryService',
    function($scope, $routeParams, subCategoryService) {
        $scope.responseMessage = "";
        getSubCategory();

        function getSubCategory() {
            subCategoryService.getSubCategory($routeParams.id)
                .then(function (subcategory) {
                    $scope.subcategory = subcategory.data;
                }
            );
        }

        $scope.updateSubCategory = function () {
            subCategoryService.updateSubCategory($scope.subcategory.id, $scope.subcategory.name)
                .then(function(response){
                    if (response.status == 200) $scope.responseMessage = "Berhasil merubah kategori";
                });
        };
    }
]);

posControllers.controller('SubCategoryCreateCtrl', ['$scope', '$location', 'categoryService', 'subcategoryService',
    function($scope, $location, categoryService, subCategoryService) {
        $scope.categories = [];
        getCategories();

        function getCategories() {
            categoryService.getCategories()
                .then(
                function (categories) {
                    $scope.categories = categories.data;
                }
            );
        }
    }
]);
