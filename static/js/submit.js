$(function() {
    function isUrlValid(url) {
        var re = /^(https?|s?ftp):\/\/(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$/i
        return re.test(url);
    }
    function isValidEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}


    $("#btnSubmit").click(function() {
         //Validate URL, Check if it is an Amazon URL, Check if it is a product URL, if possible check if product exists
        console.log("Entered btnSubmit")
        // if (!isUrlValid($("#inputPassword").val())) {
        //     // $("#url_error").removeAttr("style");
        //     // $("#url_error").text("Invalid url");1
        //     $("#emailError").innerHTML = "Invalid"
        //     return false
        // }
        var emailissues = 0
        var urlissues = 0
        if (!$("#inputEmail").val()) {
            $("#emailError").text("Email is required");
            emailissues=1;
        }
        else {
            if(!isValidEmail($("#inputEmail").val())){
               $("#emailError").text("Invalid email. Please enter a valid email");
               emailissues=1;
            }
        }
        if (!$("#inputPassword").val()) {
            $("#passError").text("URL is required");
            urlissues=1;
        }
        else {
            if(!isUrlValid($("#inputPassword").val())) {
               $("#passError").text("Invalid URL. Please enter a valid Amazon product URL");
               urlissues=1;
            }
        }



        if (urlissues==1 && emailissues==1) {
            return false;
        }

        else if (urlissues==1){
            $("#emailError").text("");
            return false;
        }
        else if (emailissues==1) {
            $("#passError").text("");
            return false;
        }
        else {
            $("#passError").text("")
            $("#emailError").text("")
        }


        $.ajax({
            url: '/submit',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response["html"]);
                //$("#disp").text(response['html']);
              
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});