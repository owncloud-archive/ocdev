

/**
 * {{ resource.name.title() }}
 */
use \OCA\AppFramework\Controller\{{ resource.name.title() }}Controller;
use \OCA\AppFramework\Service\{{ resource.name.title() }}Service;
use \OCA\AppFramework\Db\{{ resource.name.title() }}Mappper;

$this['{{ resource.name.title() }}Controller'] = $this->share(function($c){
	return new {{ resource.name.title() }}Controller(
		$c['API'],
		$c['Request'],
		$c['{{ resource.name.title() }}Service']);
});

$this['{{ resource.name.title() }}Service'] = $this->share(function($c){
	return new {{ resource.name.title() }}Service(
		$c['API'],
		$c['Request'],
		$c['{{ resource.name.title() }}Mapper']);
});

$this['{{ resource.name.title() }}Mapper'] = $this->share(function($c){
	return new {{ resource.name.title() }}Mapper(
		$c['API'],
		$c['Request']);
});