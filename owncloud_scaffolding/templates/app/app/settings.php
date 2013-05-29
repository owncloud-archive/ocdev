<?php
{% include 'licenses/licenses.php' %}

OCP\User::checkAdminUser();

OCP\Util::addScript( "{{ app.id }}", "admin" );

$tmpl = new OCP\Template( '{{ app.id }}', 'settings');

$tmpl->assign('url', OCP\Config::getSystemValue( "somesetting", '' ));

return $tmpl->fetchPage();
