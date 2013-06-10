<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Admin;

use OCA\AppFramework\App;

use OCA\{{ app.namespace }}\DependencyInjection\DIContainer;


return App::part('SettingsController', 'index', array(), new DIContainer());

