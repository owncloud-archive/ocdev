<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }};

use \OCA\AppFramework\App;
use \OCA\{{ app.namespace }}\DependencyInjection\DIContainer;


/**
 * Webinterface
 */
$this->create('{{ app.id }}_index', '/')->get()->action(
	function($params){
		App::main('PageController', 'index', $params, new DIContainer());
	}
);
