$(function(){
	$('#btnCheck').click(function(){
		
		$.ajax({
			url: '/check',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				window.alert(response);
			},
			error: function(error){
				window.alert(error);
			}
		});
	});
});
