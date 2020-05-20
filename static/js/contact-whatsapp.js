// AJAX for posting
function contact_whatsapp(form) {
    $body = $("body");
    $body.addClass("loading");
    $.ajax({
        url : form.attr("data-ajax-target"), // the endpoint
        type : "POST", // http method
        data : {
            name : $('#whats_name').val(),
            phone : $('#whats_tel').val(),
            email : $('#whats_email').val()
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            if (json.status == true) {
                $('#whatsapp-form').html("");
            }
            $('#whats_results').html(json.result);
            $body.removeClass("loading");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#whats_results').html("Oops! Nós encontramos um erro: "+errmsg); // add the error to the dom
            console.error(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            $body.removeClass("loading");
        }
    });
};


// Submit post on submit
const form = $('#whatsapp-form');
form.on('submit', function(event){
    event.preventDefault();
    contact_whatsapp(form);
});
