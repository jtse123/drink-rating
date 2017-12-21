(function() {
    var app = angular.module('drinkProj', ['ngMaterial', 'textAngular', 'ngMessages']);
    var gem = {test_name: 'Azurite'};

    app.config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });


    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    app.controller('ProjectController', function ($scope) {
        this.product = gem;
        $scope.name = "John"
    });
})();