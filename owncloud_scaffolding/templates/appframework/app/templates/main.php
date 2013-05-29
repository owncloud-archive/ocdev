{% raw %}
{{ script('public/app', 'appframework') }}
{{ script('vendor/angular/angular', 'appframework') }}
{{ script('public/app') }}
{{ style('style') }}
{% endraw %}

<div id="app" ng-app="{{ app.namespace }}" ng-cloak>

{% raw %}
<script type="text/ng-template" id="main.html">
	{% include 'partials/main.php' %}
</script>

	<div id="app-navigation">

		<ul class="with-icon" data-id="0" droppable>
			{% include 'nav.php' %}
		</ul>

		<div id="app-settings">
			{% include 'settings.php' %}
		</div>

	</div>

	<div id="app-content" ng-view></div>

</div>
{% endraw %}