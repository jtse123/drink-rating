(function() {
    var app = angular.module('drinkProj', ['ngMaterial', 'textAngular', 'ngMessages']);

    // allows us to use {$ $} in the html template to read angular instead of {{ }}
    app.config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });


    // CSRF Support
    app.config(['$httpProvider', function($httpProvider) {
         $httpProvider.defaults.xsrfCookieName = 'csrftoken';
         $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
     }]);

    app.controller('ProjectController', function ($http, $scope) {
        $scope.name = "John";

        $scope.comments_data = [];

        // finds drink id of page and then calls a get request to that specific json
        var drink = document.getElementsByClassName("drink_id")[0];
        drink_id = drink.innerText;

         $http.get('/ratings_list/'.concat(drink_id)).success(function(data){
            $scope.comments_data = data;
        })

    });
})();