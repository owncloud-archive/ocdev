{% include 'licenses/licenses.php' %}

angular.module('{{ app.namespace }}', ['Restangular']).
	config(
		['$routeProvider', '$interpolateProvider', '$windowProvider',
		function ($routeProvider, $interpolateProvider, $windowProvider) {

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

	// dynamically set base URL for HTTP requests, assume that there is no other
	// index.php in the routes
	var $window = $windowProvider.$get();
	var url = $window.location.href;
	var baseUrl = url.split('index.php')[0] + 'index.php/apps/{{ app.id }}';
	RestangularProvider.setBaseUrl(baseUrl);

	// Always send the CSRF token by default
	$httpProvider.defaults.headers.common.requesttoken = oc_requesttoken;

}]);