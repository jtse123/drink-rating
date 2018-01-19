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
        $scope.comments_data = [];

        // finds drink id of page and then calls a get request to that specific json
        var drink = document.getElementsByClassName("drink_id")[0];
        $scope.drink_id = drink.innerText;

        $scope.ip_map = [];

        // captures ip address of person on page from html template. Then uses that ip address if user posts rating
        var html_ip = document.getElementsByClassName("ip")[0];
        $scope.ip = html_ip.innerText;

         $http.get('/ratings_list/'.concat($scope.drink_id)).success(function(data){
            $scope.comments_data = data;
            $scope.rating_sum = 0;
            $scope.numOfRatings = $scope.comments_data.length;
            // calculates sum of all ratings
            for (i=0;i<$scope.comments_data.length; i++) {
                $scope.rating_sum += $scope.comments_data[i].rating;
                $scope.ip_map.push($scope.ip)
            }
            // find average of rating and round to nearest 0.5 decimal place
            $scope.avg_rating = $scope.rating_sum/$scope.comments_data.length;
            $scope.avg_rating = (Math.round($scope.avg_rating*2)/2);
            console.log($scope.ip_map)
            // console.log($scope.avg_rating);
        });

         $scope.submit = function() {
             // Checks to see if ip address already exists
             if (! $scope.ip_map.includes($scope.ip))
             {
                 $http.post('/ratings_list/'.concat($scope.drink_id).concat('/'),
                     {
                         id: $scope.id,
                         ip_address: $scope.ip,
                         comment: $scope.comment,
                         post_date: $scope.post_date,
                         drink: $scope.drink_id, //pulls drink_id from html doc
                         rating: $scope.rating
                     })
                     .then(function successCallback(response) {
                         console.log(response.data.rating);
                         console.log($scope.comments_data);
                         $scope.ip_map.push($scope.ip);
                         console.log($scope.ip_map);
                         $scope.comments_data.push(response.data);


                     }, function errorCallback() {
                         console.log('it failed')
                     });
             }
         }

    });
})();