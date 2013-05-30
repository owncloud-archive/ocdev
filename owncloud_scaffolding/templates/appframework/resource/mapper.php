<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Db;

use \OCA\AppFramework\Core\API;
use \OCA\AppFramework\Db\Mapper;
use \OCA\AppFramework\Db\Entity;

class {{ resource.name.title() }}Mapper extends Mapper {


	public function __construct (API $api) {
		parent::__construct($api, '{{ resource.name }}');
	}


}