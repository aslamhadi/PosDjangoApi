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

posControllers.controller('ProductUpdateCtrl', ['$scope', '$routeParams', 'productService',
    function($scope, $routeParams, productService) {
        $scope.responseMessage = "";
        getProduct();

        function getProduct() {
            productService.getProduct($routeParams.id)
                .then(function (product) {
                    $scope.product = product.data;
                }
            );
        }

        $scope.updateProduct = function () {
            productService.updateProduct($scope.product.id, $scope.product.name)
                .then(function(response){
                    if (response.status == 200){
                        $scope.responseMessage = "Berhasil merubah produk";
                        $scope.alert = "alert alert-success";
                    }
                });
        };
    }
]);