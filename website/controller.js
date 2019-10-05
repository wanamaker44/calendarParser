function sendTextToConvert(content) {
	var calData = content;
    $.ajax({
        type: "POST",
        url: "/sendpayload",
        data: content,
        headers: {},
        success: function(e) {
        	alert('Got it!');



        },
        error: function(e, a, t) {
            alert('Not connected!');
        }
    })
}