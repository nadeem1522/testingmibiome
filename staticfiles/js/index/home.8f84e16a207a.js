var statsAnimation = false;

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

$(window).scroll(function() {
    let windscroll = $(window).scrollTop() + screen.availHeight*0.4;
    let statsPosition = $('#stats-section').position().top;
    statsPosition = statsPosition;
    if (statsPosition < windscroll && !statsAnimation) {
        triggerAnimation('stats-1', 0, 700);
        triggerAnimation('stats-2', 0, 500);
        triggerAnimation('stats-3', 0, 15);
        statsAnimation = true;
    }
});

var triggerAnimation = async function(id, start, end) {
    let target = $(`#${id} .value`);
    if (end <= 100) {
        for (let i = start; i <= end; i++) {
            await sleep(1000/end);
            target.html(i);
        }
    } else {
        for (let i = start; i <= end; i+=25) {
            await sleep(1000*25/end);
            target.html(i);
        }
    }
}

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
            url: '/contact-us/',
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