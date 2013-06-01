<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Admin;

use OCA\AppFramework\App;

use OCA\{{ app.namespace }}\DependencyInjection\DIContainer;


// we need to fetch the output and return it for the admin page. Dont ask why
ob_start();

App::main('SettingsController', 'index', array(), new DIContainer());

$content = ob_get_contents();
ob_clean();

return $content; 
