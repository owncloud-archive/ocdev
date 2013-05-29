<?php

namespace OCA\{{ appName.namespace }};

use \OCA\AppFramework\Core\API;


// dont break owncloud when the appframework is not enabled
if(\OCP\App::isEnabled('appframework')){

	$api = new API('{{ appName.id }}');

	$api->addNavigationEntry(array(

		// the string under which your app will be referenced in owncloud
		'id' => $api->getAppName(),

		// sorting weight for the navigation. The higher the number, the higher
		// will it be listed in the navigation
		'order' => 10,

		// the route that will be shown on startup
		'href' => $api->linkToRoute('{{ appName.id }}_index'),

		// the icon that will be shown in the navigation
		// this file needs to exist in img/example.png
		'icon' => $api->imagePath('{{ appName.id }}.svg'),

		// the title of your application. This will be used in the
		// navigation or on the settings page of your app
		'name' => $api->getTrans()->t('{{ appName.full }}')

	));

} else {
	$msg = 'Can not enable the {{ appName.full }} app because the App Framework App is disabled';
	\OCP\Util::writeLog('{{ appName.id }}', $msg, \OCP\Util::ERROR);
}