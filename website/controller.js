function sendTextToConvert(content) {
	var calData = content;
    $.ajax({
        type: "POST",
        url: "https://m7axetvuse.execute-api.us-east-1.amazonaws.com/default/calendarParser",
        data: content,
        contentType: 'text/json',
        processData: false,
        headers: {},
        success: function(resp) {
        	console.log(resp);
        },
        error: function(e, a, t) {
            alert('Not connected!', e);
        }
    })
}