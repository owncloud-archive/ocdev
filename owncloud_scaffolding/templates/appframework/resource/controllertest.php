<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Controller;

use \OCA\AppFramework\Http\Request;
use \OCA\AppFramework\Http\JSONResponse;
use \OCA\AppFramework\Utility\ControllerTestUtility;


require_once(__DIR__ . "/../../classloader.php");


class {{ resource.name.title() }}ControllerTest extends ControllerTestUtility {

	private $api;
	private $request;
	private $controller;

	/**
	 * Gets run before each test
	 */
	public function setUp(){
		$this->api = $this->getAPIMock();
		$this->request = new Request();
		$this->controller = new {{ resource.name.title() }}Controller($this->api, $this->request);
	}


	public function testGetAllAnnotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption', 'Ajax');
		$this->assertAnnotations($this->controller, 'getAll', $annotations);
	}

	public function testGetAll(){
		$response = $this->controller->getAll();
		$this->assertTrue($response instanceof JSONResponse);
	}


	public function testGetAnnotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption', 'Ajax');
		$this->assertAnnotations($this->controller, 'get', $annotations);
	}

	public function testGet(){
		$response = $this->controller->get();
		$this->assertTrue($response instanceof JSONResponse);
	}

	public function testGETAnnotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption', 'Ajax');
		$this->assertAnnotations($this->controller, 'get', $annotations);
	}

	public function testGET(){
		$response = $this->controller->get();
		$this->assertTrue($response instanceof JSONResponse);
	}


	public function testCreateAnnotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption', 'Ajax');
		$this->assertAnnotations($this->controller, 'create', $annotations);
	}

	public function testCreate(){
		$response = $this->controller->create();
		$this->assertTrue($response instanceof JSONResponse);
	}



	public function testUpdateAnnotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption', 'Ajax');
		$this->assertAnnotations($this->controller, 'update', $annotations);
	}

	public function testUpdate(){
		$response = $this->controller->update();
		$this->assertTrue($response instanceof JSONResponse);
	}


	public function testDeleteAnnotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption', 'Ajax');
		$this->assertAnnotations($this->controller, 'delete', $annotations);
	}

	public function testDelete(){
		$response = $this->controller->delete();
		$this->assertTrue($response instanceof JSONResponse);
	}
}