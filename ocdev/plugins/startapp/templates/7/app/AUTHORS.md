# Authors
{% for author in app.authors %}
* {% if author.homepage %}[{{ author.name }}]({{ author.homepage }}): <{{ author.email }}>{% else %}{{ author.name }}: <{{ author.email }}>{% endif %}
{% endfor %}

