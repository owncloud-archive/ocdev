<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Controller;

use \OCA\AppFramework\Http\Request;
use \OCA\AppFramework\Http\TemplateResponse;
use \OCA\AppFramework\Utility\ControllerTestUtility;


class SettingsControllerTest extends ControllerTestUtility {

	private $api;
	private $request;
	private $controller;

	/**
	 * Gets run before each test
	 */
	public function setUp(){
		$this->api = $this->getAPIMock();
		$this->request = new Request();
		$this->controller = new SettingsController($this->api, $this->request);
	}


	public function testIndexAnnotations(){
		$annotations = array('CSRFExemption');
		$this->assertAnnotations($this->controller, 'index', $annotations);
	}

	public function testIndex(){
		$response = $this->controller->index();
		$this->assertEquals('admin/settings', $response->getTemplateName());
		$this->assertTrue($response instanceof TemplateResponse);
	}


}