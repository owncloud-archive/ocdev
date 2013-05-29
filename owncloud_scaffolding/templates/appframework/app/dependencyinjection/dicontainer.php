<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\DependencyInjection;

use \OCA\AppFramework\DependencyInjection\DIContainer as BaseContainer;

use \OCA\{{ app.namespace }}\Controller\PageController;


class DIContainer extends BaseContainer {


	/**
	 * Define your dependencies in here
	 */
	public function __construct(){
		// tell parent container about the app name
		parent::__construct('{{ app.id }}');


		/** 
		 * CONTROLLERS
		 */
		$this['PageController'] = $this->share(function($c){
			return new PageController($c['API'], $c['Request']);
		});
		

	}
}
