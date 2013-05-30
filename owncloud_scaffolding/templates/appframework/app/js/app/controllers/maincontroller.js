{% include 'licenses/licenses.php' %}

angular.module('{{ app.namespace }}').controller('MainController',
	['$scope', '$routeParams', function ($scope, $routeParams) {

	$scope.id = $routeParams.id;

}]);