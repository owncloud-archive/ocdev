<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Db;

use \OCA\{{ app.namespace }}\DependencyInjection\DIContainer;


class {{ resource.name.title() }}MapperTest extends \OCA\AppFramework\Utility\MapperTestUtility {

	private $container;

	/**
	 * Gets run before each test
	 */
	public function setUp(){
		$this->container = new DIContainer();
		$this->container['API'] = $this->getMockBuilder(
			'\OCA\AppFramework\Core\API')
			->disableOriginalConstructor()
			->getMock();
	}


}
