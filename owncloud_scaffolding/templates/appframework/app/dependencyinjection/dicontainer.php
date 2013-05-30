<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\DependencyInjection;

use \OCA\AppFramework\DependencyInjection\DIContainer as BaseContainer;


class DIContainer extends BaseContainer {


	public function __construct(){
		parent::__construct('{{ app.id }}');
		require_once __DIR__ . '/diconfig.php';
	}


}
