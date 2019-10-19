function sendTextToConvert(content) {
	var calData = content;
    $.ajax({
        type: "POST",
        url: "https://1nil08k2bg.execute-api.us-east-2.amazonaws.com/default/softballcalendarparser",
        data: content,
        headers: {},
        success: function(resp) {
        	console.log(resp);



        },
        error: function(e, a, t) {
            alert('Not connected!');
        }
    })
}