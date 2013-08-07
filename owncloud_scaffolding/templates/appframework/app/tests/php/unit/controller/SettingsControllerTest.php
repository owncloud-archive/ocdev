<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Controller;

use \OCA\AppFramework\Http\Request;
use \OCA\AppFramework\Http\TemplateResponse;
use \OCA\AppFramework\Utility\ControllerTestUtility;

use \OCA\{{ app.namespace }}\DependencyInjection\DIContainer;


class SettingsControllerTest extends ControllerTestUtility {

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


	public function testIndexAnnotations(){
		$annotations = array('CSRFExemption');
		$this->assertAnnotations($this->container['SettingsController'], 'index', 
			$annotations);
	}

	public function testIndex(){
		$response = $this->container['SettingsController']->index();
		$this->assertEquals('admin/settings', $response->getTemplateName());
		$this->assertTrue($response instanceof TemplateResponse);
	}


}