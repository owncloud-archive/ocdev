{% include 'licenses/licenses.php' %}

// define your routes in here
angular.module('{{ app.namespace }}').config(['$routeProvider', function ($routeProvider) {

	$routeProvider.when('/', {
		templateUrl: 'main.html'

	}).otherwise({
		redirectTo: '/'
	});

}]);