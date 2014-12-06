<?php
{% include app.small_license_header %}

namespace OCA\{{ app.namespace }}\Controller;

use \OCP\AppFramework\Http\TemplateResponse;
use \OCA\{{ app.namespace }}\AppInfo\Application;

class PageControllerTest extends \PHPUnit_Framework_TestCase {
	/** @var \OCP\AppFramework\IAppContainer */
	private $container;

	/** @var \OCA\{{ app.namespace }}\Controller\PageController */
	private $pageController;

	public function setUp() {
		parent::setUp();
		$app = new Application();
		$phpunit = $this;
		$this->container = $app->getContainer();
		$this->container->registerService('Request', function($c) use ($phpunit) {
			return $phpunit->getMockBuilder('\OCP\IRequest')->getMock();
		});
		$this->container->registerParameter('UserId', 'john');
		$this->pageController = $this->container->query('PageController');
	}


	public function testIndex() {
		$result = $this->pageController->index();

		$this->assertEquals(['user' => 'john'], $result->getParams());
		$this->assertEquals('main', $result->getTemplateName());
		$this->assertTrue($result instanceof TemplateResponse);
	}


	public function testEcho() {
		$result = $this->pageController->ajax();
		$this->assertEquals(['echo' => 'hi'], $result->getData());
	}


}
