

/**
 * {{ resource.name.title() }}
 */
$this->create('{{ app.id }}_{{ resource.name }}_get', '/{{ resource.name }}')->get()->action(
	function($params){
		App::main('{{ resource.name.title() }}Controller', 'get', $params, new DIContainer());
	}
);

$this->create('{{ app.id }}_{{ resource.name }}_create', '/{{ resource.name }}')->post()->action(
	function($params){
		App::main('{{ resource.name.title() }}Controller', 'create', $params, new DIContainer());
	}
);

$this->create('{{ app.id }}_{{ resource.name }}_update', '/{{ resource.name }}')->put()->action(
	function($params){
		App::main('{{ resource.name.title() }}Controller', 'update', $params, new DIContainer());
	}
);

$this->create('{{ app.id }}_{{ resource.name }}_delete', '/{{ resource.name }}')->delete()->action(
	function($params){
		App::main('{{ resource.name.title() }}Controller', 'delete', $params, new DIContainer());
	}
);