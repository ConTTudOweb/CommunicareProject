$(function() {

    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});


// AJAX for posting
function contact() {
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
            $('#id_name').val(''); // remove the value from the input name
            $('#id_email').val(''); // remove the value from the input email
            $('#id_phone').val(''); // remove the value from the input phone
            $('#id_message').val(''); // remove the value from the input message
            $('#results').html(json.result);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("Oops! Nós encontramos um erro: "+errmsg); // add the error to the dom
            console.error(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};


// AJAX for posting
function registration(form) {
    $.ajax({
        url : "/registration/", // the endpoint
        type : "POST", // http method
        data : {
            name : $('#id_name').val(),
            phone : $('#id_phone').val(),
            cpf : $('#id_cpf').val(),
            rg : $('#id_rg').val(),
            address : $('#id_address').val(),
            cep : $('#id_cep').val(),
            city : $('#id_city').val(),
            email : $('#id_email').val(),
            profession : $('#id_profession').val(),
            age : $('#id_age').val(),
            source : $('#id_source').val(),
            event_id : $('#event_id').val(),
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            console.log('success');
            $('#results').html(json.results);
            $('#errors').html(json.errors);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#errors').html("Oops! Nós encontramos um erro: "+errmsg); // add the error to the dom
            console.error(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};


// Submit post on submit
$('#contact-form').on('submit', function(event){
    event.preventDefault();
    contact();
});


// Submit post on submit
$('#registration-form').on('submit', function(event){
    event.preventDefault();
    registration();
});