$(document).on('click', '.view-password', function() {
    let icon = this.firstElementChild;
    let input = this.previousElementSibling;
    if (icon.className == 'fa fa-eye') {
        icon.className = 'fa fa-eye-slash';
        input.type = 'text';
    } else {
        icon.className = 'fa fa-eye';
        input.type = 'password';
    }
});

var addMessage = function(id, className, mess, padding) {
    $(`#${id}`).addClass(className);
    $(`#${id}`).text(mess);
    $(`#${id}`).css(`padding-${padding}`, '1rem');
}

var removeMessage = function(id, className, padding, timeout=10000) {
    setTimeout(function() {
        $(`#${id}`).removeClass(className);
        $(`#${id}`).text('');
        $(`#${id}`).css(`padding-${padding}`, '0rem');
    }, timeout);
}