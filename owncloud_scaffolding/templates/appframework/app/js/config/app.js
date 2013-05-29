{% include 'licenses/licenses.php' %}

angular.module('{{ app.namespace }}', ['OC']).
	config(['$routeProvider', function ($routeProvider) {

	$routeProvider.when('/', {
		templateUrl: 'main.html'

	}).otherwise({
		redirectTo: '/'
	});

}]);