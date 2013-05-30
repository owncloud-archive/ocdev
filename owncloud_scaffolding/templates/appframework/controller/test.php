<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Controller;

use \OCA\AppFramework\Http\Request;
use \OCA\AppFramework\Http\JSONResponse;
use \OCA\AppFramework\Utility\ControllerTestUtility;


require_once(__DIR__ . "/../../classloader.php");


class {{ controller.name }}Test extends ControllerTestUtility {

	private $api;
	private $request;
	private $controller;

	/**
	 * Gets run before each test
	 */
	public function setUp(){
		$this->api = $this->getAPIMock();
		$this->request = new Request();
		$this->controller = new PageController($this->api, $this->request);
	}


	public function test{{ controller.methodName.title() }}Annotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption');
		$this->assertAnnotations($this->controller, '{{ controller.methodName }}', $annotations);
	}

	public function testIndex(){
		$response = $this->controller->{{ controller.methodName }}();
		$this->assertTrue($response instanceof JSONResponse);
	}


}