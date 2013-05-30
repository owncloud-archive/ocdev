<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Service;

use \OCA\AppFramework\Core\API;
use \OCA\AppFramework\Db\Mapper;
use \OCA\AppFramework\Db\Entity;

use \OCA\{{ app.namespace }}\Db\{{ resource.name.title() }}Mapper;


class {{ resource.name.title() }}Service {

	private $api;
	private $mapper;

	public function __construct (API $api, {{ resource.name.title() }}Mapper $mapper) {
		$this->api = $api;
		$this->mapper = $mapper;
	}


}