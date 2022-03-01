var enquirySent = false;

$("#contact-form").on('submit', '', function (event) {
    event.preventDefault();
    if (!enquirySent) {
        enquirySent = true;
        addMessage('contact-message', 'success', 'Please wait...');
        let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        let name = $('#name').val();
        let email = $('#email').val();
        let message = $('#message').val();
        $.ajax({
            type: 'POST',
            url: '',
            data: {
                'csrfmiddlewaretoken': csrfToken,
                'name': name,
                'email': email,
                'message': message
            },
            success: function (response) {
                if (response.status) {
                    addMessage('contact-message', 'success', response.message);
                    removeMessage('contact-message', 'success');
                    $('#name').val('');
                    $('#email').val('');
                    $('#message').val('');
                } else {
                    addMessage('contact-message', 'error', response.message);
                    removeMessage('contact-message', 'error');
                }
                enquirySent = false;
            },
            error: function (_) {
                addMessage('contact-message', 'error', 'Internal Server Error');
                removeMessage('contact-message', 'error');
                enquirySent = false;
            }
        });
    }
});