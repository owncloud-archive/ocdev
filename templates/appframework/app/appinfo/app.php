<?php

namespace OCA\{{ app.namespace }};

use \OCA\AppFramework\Core\API;


// dont break owncloud when the appframework is not enabled
if(\OCP\App::isEnabled('appframework')){

	$api = new API('{{ app.id }}');

	$api->addNavigationEntry(array(

		// the string under which your app will be referenced in owncloud
		'id' => $api->getAppName('{{ app.id }}'),

		// sorting weight for the navigation. The higher the number, the higher
		// will it be listed in the navigation
		'order' => 10,

		// the route that will be shown on startup
		'href' => $api->linkToRoute('{{ app.id }}_index'),

		// the icon that will be shown in the navigation
		// this file needs to exist in img/example.png
		'icon' => $api->imagePath('icon.svg'),

		// the title of your application. This will be used in the
		// navigation or on the settings page of your app
		'name' => $api->getTrans()->t('{{ app.fullName }}')

	));

} else {
	$msg = 'Can not enable the {{ app.full }} app because the App Framework App is disabled';
	\OCP\Util::writeLog('{{ app.id }}', $msg, \OCP\Util::ERROR);
}