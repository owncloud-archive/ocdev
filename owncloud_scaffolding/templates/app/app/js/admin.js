{% include 'licenses/licenses.php' %}

$(document).ready(function(){

	$('#somesetting').blur(function(event){
		event.preventDefault();
		var post = $( "#somesetting" ).serialize();
		$.post( OC.filePath('{{ app.id }}', 'ajax', 'seturl.php') , post, function(data){
			$('#apptemplate .msg').text('Finished saving: ' + data);
		});
	});

});
