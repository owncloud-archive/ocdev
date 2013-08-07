<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Controller;

use \OCA\AppFramework\Http\Request;
use \OCA\AppFramework\Http\JSONResponse;
use \OCA\AppFramework\Utility\ControllerTestUtility;

use \OCA\{{ app.namespace }}\DependencyInjection\DIContainer;


class {{ resource.name.title() }}ControllerTest extends ControllerTestUtility {

	private $container;

	/**
	 * Gets run before each test
	 */
	public function setUp(){
		$this->container = new DIContainer();
		$this->container['Request'] = new Request();
		$this->container['API'] = $this->getMockBuilder(
			'\OCA\AppFramework\Core\API')
			->disableOriginalConstructor()
			->getMock();
	}


	public function testGetAllAnnotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption', 'Ajax');
		$this->assertAnnotations($this->container['{{ resource.name.title() }}Controller'], 
			'getAll', $annotations);
	}

	public function testGetAll(){
		$response = $this->container['{{ resource.name.title() }}Controller']->getAll();
		$this->assertTrue($response instanceof JSONResponse);
	}


	public function testGetAnnotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption', 'Ajax');
		$this->assertAnnotations($this->container['{{ resource.name.title() }}Controller'], 
			'get', $annotations);
	}

	public function testGet(){
		$response = $this->container['{{ resource.name.title() }}Controller']->get();
		$this->assertTrue($response instanceof JSONResponse);
	}

	public function testGETAnnotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption', 'Ajax');
		$this->assertAnnotations($this->container['{{ resource.name.title() }}Controller'], 
			'get', $annotations);
	}

	public function testGET(){
		$response = $this->container['{{ resource.name.title() }}Controller']->get();
		$this->assertTrue($response instanceof JSONResponse);
	}


	public function testCreateAnnotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption', 'Ajax');
		$this->assertAnnotations($this->container['{{ resource.name.title() }}Controller'], 
			'create', $annotations);
	}

	public function testCreate(){
		$response = $this->container['{{ resource.name.title() }}Controller']->create();
		$this->assertTrue($response instanceof JSONResponse);
	}



	public function testUpdateAnnotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption', 'Ajax');
		$this->assertAnnotations($this->container['{{ resource.name.title() }}Controller'], 
			'update', $annotations);
	}

	public function testUpdate(){
		$response = $this->container['{{ resource.name.title() }}Controller']->update();
		$this->assertTrue($response instanceof JSONResponse);
	}


	public function testDeleteAnnotations(){
		$annotations = array('IsAdminExemption', 'IsSubAdminExemption', 'Ajax');
		$this->assertAnnotations($this->container['{{ resource.name.title() }}Controller'], 
			'delete', $annotations);
	}

	public function testDelete(){
		$response = $this->container['{{ resource.name.title() }}Controller']->delete();
		$this->assertTrue($response instanceof JSONResponse);
	}
}