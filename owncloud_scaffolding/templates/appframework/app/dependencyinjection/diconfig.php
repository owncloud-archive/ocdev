<?php
{% include 'licenses/licenses.php' %}


namespace OCA\{{ app.namespace }}\DependencyInjection;

use \OCA\{{ app.namespace }}\Controller\PageController;
use \OCA\{{ app.namespace }}\Controller\SettingsController;

/**
 * Delete the following twig config to use ownClouds default templates
 */
// use this to specify the template directory
$this['TwigTemplateDirectory'] = __DIR__ . '/../templates';


/**
 * CONTROLLERS
 */
$this['PageController'] = $this->share(function($c){
	return new PageController($c['API'], $c['Request']);
});

$this['SettingsController'] = $this->share(function($c){
	return new SettingsController($c['API'], $c['Request']);
});
