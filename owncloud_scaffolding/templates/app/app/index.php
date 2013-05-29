<?php
{% include 'licenses/licenses.php' %}

// Check if we are a user
OCP\User::checkLoggedIn();

$somesetting = OCP\Config::getSystemValue( "somesetting", '' );
OCP\App::setActiveNavigationEntry( '{{ app.id }}' );
$tmpl = new OCP\Template( '{{ app.id }}', 'main', 'user' );
$tmpl->assign( 'somesetting', $somesetting );
$tmpl->printPage();
