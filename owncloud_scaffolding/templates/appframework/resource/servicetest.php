<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Service;

use \OCA\{{ app.namespace }}\DependencyInjection\DIContainer;


class {{ resource.name.title() }}ServiceTest extends \OCA\AppFramework\Utility\TestUtility {

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
		$this->container['{{ resource.name.title() }}Mapper'] = $this->getMockBuilder('\OCA\{{ app.namespace }}\Db\{{ resource.name.title() }}Mapper')
			->disableOriginalConstructor()
			->getMock();
	}


}
