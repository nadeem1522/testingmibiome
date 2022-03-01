let requestSent = false;

$('form#signup-form').on('submit', '', function(event) {
    if (!requestSent) {
        requestSent = true;
        event.preventDefault();
        let title = $('#title').val().trim();
        let firstName = $('#first-name').val().trim();
        let lastName = $('#last-name').val().trim();
        let affiliation = $('#affiliation').val().trim();
        let designation = $('#designation').val().trim();
        let industry = $('#industry').val().trim();
        let phone = $('#phone').val().trim();
        let email = $('#email').val().trim();
        let password1 = $('#password').val().trim();
        let password2 = $('#confirm-password').val().trim();
        let csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
        if (password1 != password2) {
            $('#error-modal .modal-body').html('<div>Password and Confirm Password do not match</div>');
            $('#error-modal').modal('show');
            $('#password').val('');
            $('#confirm-password').val('');
            requestSent = false;
            return;
        }
        $('.spinner-border').css('display', '');
        $.ajax({
            type: 'POST',
            url: '/user/signup/',
            data: {
                'title': title,
                'first_name': firstName,
                'last_name': lastName,
                'affiliation': affiliation,
                'designation': designation,
                'industry': industry,
                'phone': phone,
                'email': email,
                'password': password1,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(response) {
                if (response.status) {
                    $('#title').val('');
                    $('#first-name').val('');
                    $('#last-name').val('');
                    $('#affiliation').val('');
                    $('#designation').val('');
                    $('#industry').val('');
                    $('#phone').val('');
                    $('#email').val('');
                    $('#password').val('');
                    $('#confirm-password').val('');
                    $('#success-modal').modal('show');
                    $('.spinner-border').css('display', 'none');
                    requestSent = false;
                } else {
                    $('#error-modal .modal-body').html(`<div>${response.message}</div>`);
                    $('#error-modal').modal('show');
                    $('.spinner-border').css('display', 'none');
                    requestSent = false;
                }
            },
            error: function(_) {
                $('#error-modal .modal-body').html(`<div>Internal Server Error</div>`);
                $('#error-modal').modal('show');
                $('.spinner-border').css('display', 'none');
                requestSent = false;
            },
        });
    }
});