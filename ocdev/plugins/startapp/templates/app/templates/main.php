<?php
\OCP\Util::addScript('{{ app.id }}', 'script');

\OCP\Util::addStyle('{{ app.id }}', 'style');

?>

<p>Hello World <?php p($_['user']) ?></p>

<p><button id="hello">click me</button></p>

<p><textarea id="echo-content">
	Send this as ajax
</textarea></p>
<p><button id="echo">Send ajax request</button></p>

Ajax response: <div id="echo-result"></div>