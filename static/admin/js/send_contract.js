
// AJAX for posting
function send_contract(registration) {
    alert(registration);
    $.ajax({
        url : "/send_contract/", // the endpoint
        type : "GET", // http method
        data : {
            pk : registration,
        }
    });
};