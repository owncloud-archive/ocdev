// compiled with grunt

(function(angular, $, oc_requesttoken, undefined){

'use strict';

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

	// because twig already uses {% raw %}{{}}{% endraw %}
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
angular.module('{{ app.namespace }}').controller('MainController',
	['$scope', '$routeParams', function ($scope, $routeParams) {

	$scope.id = $routeParams.id;

}]);
})(angular, jQuery, oc_requesttoken);
