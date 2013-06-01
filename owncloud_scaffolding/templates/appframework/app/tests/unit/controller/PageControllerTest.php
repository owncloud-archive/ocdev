<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Controller;

use \OCA\AppFramework\Http\Request;
use \OCA\AppFramework\Http\TemplateResponse;
use \OCA\AppFramework\Utility\ControllerTestUtility;


require_once(__DIR__ . "/../../classloader.php");


class PageControllerTest extends ControllerTestUtility {

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


	public function testIndexAnnotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption',
			'CSRFExemption');
		$this->assertAnnotations($this->controller, 'index', $annotations);
	}

	public function testIndex(){
		$response = $this->controller->index();
		$this->assertEquals('main', $response->getTemplateName());
		$this->assertTrue($response instanceof TemplateResponse);
	}


}