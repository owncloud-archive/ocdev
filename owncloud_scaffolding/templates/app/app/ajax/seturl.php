<?php
{% include 'licenses/licenses.php' %}

OCP\User::checkAdminUser();
OCP\JSON::callCheck();

OCP\Config::setSystemValue( 'somesetting', $_POST['somesetting'] );

echo 'true';
