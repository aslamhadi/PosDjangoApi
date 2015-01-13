posControllers.controller('SalesCtrl', function ($scope, $location, salesService) {
    $scope.sales = [];
    $scope.title = "Tambah Pembayaran";
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

    $scope.detailSaleLink = function (saleId) {
        $location.path('/sales/detail/' + saleId + '/');
    };
 }
);

posControllers.controller('SalesDetailCtrl', function ($scope, $routeParams, salesService) {
    $scope.title = "Detail Pembayaran";
    $scope.responseMessage = "";
    $scope.saleProducts = [];

    getSale();

    function getSale() {
        salesService.getSale($routeParams.id)
            .then(function (sale) {
                $scope.sale = sale.data;
                salesService.getSaleProducts(sale.data.id)
                    .then(function (saleProducts) {
                        $scope.saleProducts = saleProducts.data;

                    });
            }
        );
    }
 }
);
