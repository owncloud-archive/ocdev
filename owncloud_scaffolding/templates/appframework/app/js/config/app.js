{% include 'licenses/licenses.php' %}

angular.module('{{ app.namespace }}', ['OC']).
	config(
		['$routeProvider', '$interpolateProvider', 
		function ($routeProvider, $interpolateProvider) {

	$routeProvider.when('/', {
		templateUrl: 'main.html',
		controller: 'MainController'
	}).when('/:id', {
		templateUrl: 'main.html',
		controller: 'MainController'
	}).otherwise({
		redirectTo: '/'
	});

	// {% raw %}because twig already uses {{}}{% endraw %}
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
}]);