<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Db;

use \OCA\AppFramework\Db\Entity;

class {{ resource.name.title() }} extends Entity {


	public function __construct () {
		parent::__construct();
	}


}