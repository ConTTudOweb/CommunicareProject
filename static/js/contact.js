// AJAX for posting
function contact() {
    $body = $("body");
    $body.addClass("loading");
    $.ajax({
        url : "contact/", // the endpoint
        type : "POST", // http method
        data : {
            name : $('#id_name').val(),
            email : $('#id_email').val(),
            phone : $('#id_phone').val(),
            message : $('#id_message').val()
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            if (json.status == true) {
                $('#id_name').val(''); // remove the value from the input name
                $('#id_email').val(''); // remove the value from the input email
                $('#id_phone').val(''); // remove the value from the input phone
                $('#id_message').val(''); // remove the value from the input message
            }
            $('#results').html(json.result);
            $body.removeClass("loading");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("Oops! Nós encontramos um erro: "+errmsg); // add the error to the dom
            console.error(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            $body.removeClass("loading");
        }
    });
};


// Submit post on submit
$('#contact-form').on('submit', function(event){
    event.preventDefault();
    contact();
});