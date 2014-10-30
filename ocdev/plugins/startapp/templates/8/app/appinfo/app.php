<?php
{% include app.small_license_header %}

namespace OCA\{{ app.namespace }}\AppInfo;


\OCP\App::addNavigationEntry(array(
    // the string under which your app will be referenced in owncloud
    'id' => '{{ app.id }}',

    // sorting weight for the navigation. The higher the number, the higher
    // will it be listed in the navigation
    'order' => 10,

    // the route that will be shown on startup
    'href' => \OCP\Util::linkToRoute('{{ app.id }}.page.index'),

    // the icon that will be shown in the navigation
    // this file needs to exist in img/
    'icon' => \OCP\Util::imagePath('{{ app.id }}', 'app.svg'),

    // the title of your application. This will be used in the
    // navigation or on the settings page of your app
    'name' => \OC_L10N::get('{{ app.id }}')->t('{{ app.name }}')
));
