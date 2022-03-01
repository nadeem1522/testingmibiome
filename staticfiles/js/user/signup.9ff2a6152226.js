$('form#signup-form').on('submit', '', function(event) {
    event.preventDefault();
    let firstName = $('#first-name').val().trim();
    let lastName = $('#last-name').val().trim();
    let phone = $('#phone').val().trim();
    let email = $('#email').val().trim();
    let password1 = $('#password').val().trim();
    let password2 = $('#confirm-password').val().trim();
    let csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    if (password1 != password2) {
        addMessage('signup-message', 'error', 'Password and Confirm Password do not match', 'bottom');
        removeMessage('signup-message', 'error', 'bottom');
        $('#password').val('');
        $('#confirm-password').val('');
        return;
    }
    $.ajax({
        type: 'POST',
        url: '/user/signup/',
        data: {
            'first_name': firstName,
            'last_name': lastName,
            'phone': phone,
            'email': email,
            'password': password1,
            'csrfmiddlewaretoken': csrftoken
        },
        success: function(response) {
            if (response.status) {
                addMessage('signup-message', 'success', response.message, 'bottom');
                removeMessage('signup-message', 'success', 'bottom');
                window.location = '/user/login/';
            } else {
                addMessage('signup-message', 'error', response.message, 'bottom');
                removeMessage('signup-message', 'error', 'bottom');
            }
        },
        error: function(_) {
            addMessage('signup-message', 'error', 'Internal Server Error', 'bottom');
            removeMessage('signup-message', 'error', 'bottom');
        },
    });
});