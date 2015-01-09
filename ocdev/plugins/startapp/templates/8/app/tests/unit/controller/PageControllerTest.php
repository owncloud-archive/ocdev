<?php
{% include app.small_license_header %}

namespace OCA\{{ app.namespace }}\Controller;

use PHPUnit_Framework_TestCase;

use OCP\AppFramework\Http\TemplateResponse;
use OCP\AppFramework\App;

class PageControllerTest extends PHPUnit_Framework_TestCase {

	private $request;
	private $pageController;
	private $userId = 'john';

	public function setUp() {
		$app = new App('{{ app.id }}');
		$this->container = $app->getContainer();

		$this->request = $this->getMockBuilder('OCP\IRequest')->getMock();
		$this->container->registerService('OCP\IRequest', function($c) {
			return $this->request;
		});

		$this->container->registerService('UserId', function($c) {
			return $this->userId;
		});

		$this->pageController = $this->container->query(
			'OCA\{{ app.namespace }}\Controller\PageController'
		);
	}


	public function testIndex() {
		$result = $this->pageController->index();

		$this->assertEquals(['user' => 'john'], $result->getParams());
		$this->assertEquals('main', $result->getTemplateName());
		$this->assertTrue($result instanceof TemplateResponse);
	}


	public function testEcho() {
		$result = $this->pageController->doEcho('hi');
		$this->assertEquals(['echo' => 'hi'], $result->getData());
	}


}
