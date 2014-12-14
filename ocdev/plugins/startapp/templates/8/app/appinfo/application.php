<?php
{% include app.small_license_header %}

namespace OCA\{{ app.namespace }}\AppInfo;

use \OCP\AppFramework\App;
use \OCP\IContainer;

class Application extends App {


	public function __construct (array $urlParams=[]) {
		parent::__construct('{{ app.id }}', $urlParams);

		$container = $this->getContainer();


		/**
		 * Core
		 */
		$container->registerService('UserId', function(IContainer $c) {
			return \OCP\User::getUser();
		});
	}


}
