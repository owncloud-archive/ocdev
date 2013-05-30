<?php
{% include 'licenses/licenses.php' %}

require_once(__DIR__ . "/../../classloader.php");

namespace OCA\{{ app.namespace }}\Service;


class {{ resource.name.title() }}ServiceTest extends \OCA\AppFramework\Utility\TestUtility {

	private $service;
	private $api;
	private $mapper;
	
	protected function setUp(){
		$this->api = $this->getMockBuilder('\OCA\AppFramework\Core\API')
			->disableOriginalConstructor()
			->getMock();
		$this->mapper = $this->getMockBuilder('\OCA\{{ app.namespace }}\Db\{{ resource.name.title() }}Mapper')
			->disableOriginalConstructor()
			->getMock();

		$this->service = new {{ resource.name.title() }}Service($this->api, $this->mapper);
	}


}
