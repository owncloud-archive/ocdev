<?php
{% include 'licenses/licenses.php' %}

namespace OCA\{{ app.namespace }}\Controller;

use \OCA\AppFramework\Controller\Controller;
use \OCA\AppFramework\Core\API;
use \OCA\AppFramework\Http\Request;


class PageController extends Controller {


	public function __construct(API $api, Request $request){
		parent::__construct($api, $request);
	}


	/**
	 * ATTENTION!!!
	 * The following comment turns off security checks
	 * Please look up their meaning in the documentation!
	 *
	 * @IsAdminExemption
	 * @IsSubAdminExemption
	 * @CSRFExemption
	 */
	public function index() {
		return $this->render('main');
	}


}