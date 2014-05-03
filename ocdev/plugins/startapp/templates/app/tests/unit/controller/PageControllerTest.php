<?php
{% include app.small_license_header %}

namespace OCA\{{ app.namespace }}\Controller;


use \OCP\IRequest;
use \OCP\AppFramework\Http\TemplateResponse;
use \OCP\AppFramework\Http\JSONResponse;

use \OCA\{{ app.namespace }}\AppInfo\Application;


class PageControllerTest extends \PHPUnit_Framework_TestCase {

	private $container;

	public function setUp () {
		$app = new Application();
		$this->container = $app->getContainer();
	}


	public function testIndex () {
		// swap out request
		$this->container['Request'] = $this->getRequest();
		$this->container['UserId'] = 'john';

		$result = $this->container['PageController']->index();

		$this->assertEquals(array('user' => 'john'), $result->getParams());
		$this->assertEquals('main', $result->getTemplateName());
		$this->assertTrue($result instanceof TemplateResponse);
	}


	public function testEcho () {
		$this->container['Request'] = $this->getRequest(array(
			'post' => array('echo' => 'hi')
		));

		$result = $this->container['PageController']->doEcho();

		$this->assertEquals(array('echo' => 'hi'), $result->getData());
		$this->assertTrue($result instanceof JSONResponse);	
	}


	/**
	 * Instead of using positional parameters this function instantiates
	 * a request by using a hashmap so its easier to only set specific params
	 * @param array $params a hashmap with the parameters for request
	 * @return Request a request instance
	 */
	private function getRequest(array $params=array()) {
		$mock = $this->getMockBuilder('\OCP\IRequest')
			->getMock();

		$merged = array();

		foreach ($params as $key => $value) {
			$merged = array_merge($value, $merged);
		}

		$mock->expects($this->any())
			->method('getParam')
			->will($this->returnCallback(function($index, $default) use ($merged) {
				if (array_key_exists($index, $merged)) {
					return $merged[$index];
				} else {
					return $default;
				}
			}));

		// attribute access, only server implemented for now
		if(array_key_exists('server', $params)) {
			$mock->server = $params['server'];
		}

		return $mock;
	}

}