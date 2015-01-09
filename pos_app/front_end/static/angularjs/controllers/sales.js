posControllers.controller('SalesCtrl', function ($scope, $location, salesService) {
    $scope.sales = [];
    $scope.title = "Tambah Pembayaran"
    $scope.addResponse = "";

    getSales()
    function getSales() {
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
    getSale();

    function getSale() {
        salesService.getSale($routeParams.id)
            .then(function (sale) {
                $scope.sale = sale.data;
            }
        );
    }
 }
);
