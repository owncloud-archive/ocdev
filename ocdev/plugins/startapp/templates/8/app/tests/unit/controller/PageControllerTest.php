<?php
{% include app.small_license_header %}

namespace OCA\{{ app.namespace }}\Controller;

use PHPUnit_Framework_TestCase;

use OCP\AppFramework\Http\TemplateResponse;
use OCP\AppFramework\App;

class PageControllerTest extends PHPUnit_Framework_TestCase {

	private $request;
	private $controller;
	private $userId = 'john';

	public function setUp() {
		$app = new App('{{ app.id }}');
		$container = $app->getContainer();

		$this->request = $this->getMockBuilder('OCP\IRequest')->getMock();
		$container->registerService('OCP\IRequest', function($c) {
			return $this->request;
		});

		$container->registerService('UserId', function($c) {
			return $this->userId;
		});

		$this->controller = $container->query(
			'OCA\{{ app.namespace }}\Controller\PageController'
		);
	}


	public function testIndex() {
		$result = $this->controller->index();

		$this->assertEquals(['user' => 'john'], $result->getParams());
		$this->assertEquals('main', $result->getTemplateName());
		$this->assertTrue($result instanceof TemplateResponse);
	}


	public function testEcho() {
		$result = $this->controller->doEcho('hi');
		$this->assertEquals(['echo' => 'hi'], $result->getData());
	}


}
