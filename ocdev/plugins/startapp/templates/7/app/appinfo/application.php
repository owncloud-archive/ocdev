<?php
{% include app.small_license_header %}

namespace OCA\{{ app.namespace }}\AppInfo;


use \OCP\AppFramework\App;
use \OCP\AppFramework\IAppContainer;

use \OCA\{{ app.namespace }}\Controller\PageController;


class Application extends App {


	public function __construct (array $urlParams=array()) {
		parent::__construct('{{ app.id }}', $urlParams);

		$container = $this->getContainer();

		/**
		 * Controllers
		 */
		$container->registerService('PageController', function(IAppContainer $c) {
			return new PageController(
				$c->query('AppName'), 
				$c->query('Request'),
				$c->query('UserId')
			);
		});


		/**
		 * Core
		 */
		$container->registerService('UserId', function(IAppContainer $c) {
			return \OCP\User::getUser();
		});		
		
	}


}
