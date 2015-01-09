posControllers.controller('SalesCtrl', function ($scope, $location, salesService) {
        $scope.sales = [];
        $scope.title = "Tambah Pembayaran"
        $scope.addResponse = "";

        getPayments();

        function getPayments() {
            salesService.getSales()
                .then(
                function (sales) {
                    $scope.sales = sales.data;
                }
            );
        }
    }
);

posControllers.controller('SalesUpdateCtrl', function ($scope, $routeParams, salesService) {
        $scope.title = "Update Pembayaran";
        $scope.responseMessage = "";
        getPayment();

        function getPayment() {
            salesService.getSale($routeParams.id)
                .then(function (sale) {
                    $scope.sale = sale.data;
                }
            );
        }
    }
);
