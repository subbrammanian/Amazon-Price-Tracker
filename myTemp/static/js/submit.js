$(function() {
  $('#btnSubmit').bind('click', function() {
	$.ajax({
		url:'/submit',
		data: $('#cform').serialize(),
		type: 'post',
		success: function(data){
			console.log(data)
		}
	})
  });
});



// $(function() {
//   $('#btnSubmit').bind('click', function() {
// 	$.getJSON('/submit', {
// 	  email: $('input[name="inpEmail"]').val(),url: $('input[name="inpPassword"]').val()
// 	}, function(data) {
// 	  $("#result").text(data.result);
// 	  $("#cform")[0].reset();
// 	});
//   });
// });