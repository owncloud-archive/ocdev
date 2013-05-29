{% include 'licenses/licenses.php' %}

describe('MainController', function() {

	var controller;

	// use the news container
	beforeEach(module('News'));

	beforeEach(inject(function ($controller, $rootScope) {
		controller = $controller('MainController', {
			$scope: $rootScope.$new()
		});
	}));


	it('should work', function () {
		expect(2+2).toBe(4);
	});


});