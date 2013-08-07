{% raw %}
{{ script('vendor/angular/angular') }}
{{ script('vendor/underscore/underscore') }}
{{ script('vendor/restangular/restangular') }}
{{ script('public/app') }}
{{ style('style') }}
{% endraw %}

<div id="app" ng-app="{{ app.namespace }}" ng-cloak>

{% raw %}
<script type="text/ng-template" id="main.html">
	{% include 'partials/main.php' %}
</script>

	<div id="app-navigation">

		<ul class="with-icon">
			{% include 'nav.php' %}
		</ul>

		<div id="app-settings">
			{% include 'settings.php' %}
		</div>

	</div>

	<div id="app-content" ng-view></div>

</div>
{% endraw %}