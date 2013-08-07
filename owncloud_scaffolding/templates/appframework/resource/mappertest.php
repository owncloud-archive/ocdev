<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Db;


class {{ resource.name.title() }}MapperTest extends \OCA\AppFramework\Utility\MapperTestUtility {

	private $mapper;
	private $api;


	protected function setUp(){
		$this->api = $this->getMockBuilder('\OCA\AppFramework\Core\API')
			->disableOriginalConstructor()
			->getMock();

		$this->mapper = new {{ resource.name.title() }}Mapper($this->api);
	}


}
