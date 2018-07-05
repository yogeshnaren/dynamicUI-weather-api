$(document).ready(function() {
	$("#reset").click(function(){
		$("#inp").val('');
	});
	$(".operator").click(function(){
		var val = $("#inp").val();
		$("#inp").val(val + $(this).attr('data-operator'));
	});
	$("#calculate").click(function(){
		$.ajax({
		  url: '',
		  contentType: 'text/plain',
		  dataType: 'string',
		  data: $("#inp").val(),
		  success: function(response){
				$("#inp").val(response);
		  },
		  error: function(error){
			  console.log('error');
		  }
		});
	});
	$("#inp").keydown(function(e){
		var a = ['+','-','*','/','0','1','2','3','4','5','6','7','8','9'];
		if(a.indexOf(e.key) == -1)
		{
			e.preventDefault();
		}
	});
});

