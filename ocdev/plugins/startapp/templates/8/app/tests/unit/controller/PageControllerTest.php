<?php
{% include app.small_license_header %}

namespace OCA\{{ app.namespace }}\Controller;

use \OCP\AppFramework\Http\TemplateResponse;
use \OCP\AppFramework\App;

class PageControllerTest extends \PHPUnit_Framework_TestCase {
	/** @var \OCP\AppFramework\IAppContainer */
	private $container;

	/** @var \OCA\{{ app.namespace }}\Controller\PageController */
	private $pageController;

	public function setUp() {
		parent::setUp();
		$app = new App('{{ app.id }}');
		$phpunit = $this;
		$this->container = $app->getContainer();
		$this->container->registerService('Request', function($c) use ($phpunit) {
			return $phpunit->getMockBuilder('\OCP\IRequest')->getMock();
		});
		$this->container->registerParameter('UserId', 'john');
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
