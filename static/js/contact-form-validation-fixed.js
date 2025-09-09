jQuery(document).ready(function($) {
    "use strict";
    
    // Function to get CSRF token from cookie
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    // Function to get CSRF token from meta tag
    function getCSRFToken() {
        var csrfToken = $('meta[name="csrf-token"]').attr('content');
        if (!csrfToken) {
            csrfToken = getCookie('csrftoken');
        }
        return csrfToken;
    }

    $("#contact-form").validate({
        submitHandler: function(form) {
            var $form = $(form),
                $success = $("#contactSuccess"),
                $error = $("#contactError"),
                $submitBtn = $(this.submitButton);
            
            $submitBtn.button("loading");
            
            // Get CSRF token
            var csrfToken = getCSRFToken();
            console.log("CSRF Token:", csrfToken);
            
            // Check if we have a valid CSRF token
            if (!csrfToken) {
                console.error("CSRF token not found! Falling back to form token.");
                // Try to get token from form input
                csrfToken = $form.find('input[name="csrfmiddlewaretoken"]').val();
                console.log("Form CSRF Token:", csrfToken);
            }
            
            if (!csrfToken) {
                console.error("No CSRF token available! Form submission will fail.");
                $submitBtn.button("reset");
                $error.removeClass("hidden");
                return;
            }
            
            $.ajax({
                type: "POST",
                url: $form.attr("action"),
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                },
                data: {
                    name: $form.find("#name").val(),
                    email: $form.find("#email").val(),
                    subject: $form.find("#subject").val(),
                    message: $form.find("#message").val(),
                    csrfmiddlewaretoken: csrfToken
                },
                dataType: "json",
                complete: function(response) {
                    // Handle both JSON and HTML responses
                    var isSuccess = false;
                    var responseText = response.responseText || '';
                    
                    // Check for JSON response first
                    if (typeof response.responseJSON === "object") {
                        if (response.responseJSON.response === "success") {
                            isSuccess = true;
                        }
                    }
                    // Fallback: check HTML response for success indicators
                    else if (responseText.toLowerCase().includes('success') ||
                             responseText.toLowerCase().includes('message sent') ||
                             window.location.href.includes('status=success')) {
                        isSuccess = true;
                    }
                    
                    if (isSuccess) {
                        $success.removeClass("hidden");
                        $error.addClass("hidden");
                        $form.find(".controled").val("").blur().parent().removeClass("has-success").removeClass("has-error").find("label.error").remove();
                        $form.find(".controled").removeClass("error");
                        if ($success.offset().top - 80 < $(window).scrollTop()) {
                            $("html, body").animate({scrollTop: $success.offset().top - 80}, 300);
                        }
                        $submitBtn.button("reset");
                        $(".controled").keyup(function() {
                            $success.addClass("hidden");
                        });
                    } else {
                        $error.removeClass("hidden");
                        $success.addClass("hidden");
                        $form.find(".controled").val("").blur().parent().removeClass("has-success").removeClass("has-error").find("label.error").remove();
                        if ($error.offset().top - 80 < $(window).scrollTop()) {
                            $("html, body").animate({scrollTop: $error.offset().top - 80}, 300);
                        }
                        $form.find(".has-success").removeClass("has-success");
                        $submitBtn.button("reset");
                        $(".controled").keyup(function() {
                            $error.addClass("hidden");
                        });
                    }
                }
            });
        }
    });
});