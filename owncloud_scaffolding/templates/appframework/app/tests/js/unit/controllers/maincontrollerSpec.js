{% include 'licenses/licenses.php' %}

describe('MainController', function() {

	var controller;

	// use the {{ app.namespace }} container
	beforeEach(module('{{ app.namespace }}'));

	beforeEach(inject(function ($controller, $rootScope) {
		controller = $controller('MainController', {
			$scope: $rootScope.$new()
		});
	}));


	it('should work', function () {
		expect(2+2).toBe(4);
	});


});
