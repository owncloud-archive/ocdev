<?php
{% include 'licenses/licenses.php' %}

OCP\App::registerAdmin('{{ app.id }}', 'settings');

OCP\App::addNavigationEntry( array( 
	'id' => '{{ app.id }}',
	'order' => 74,
	'href' => OCP\Util::linkTo( '{{ app.id }}', 'index.php' ),
	'icon' => OCP\Util::imagePath( '{{ app.id }}', 'icon.png' ),
	'name' => '{{ app.fullName }}'
));
