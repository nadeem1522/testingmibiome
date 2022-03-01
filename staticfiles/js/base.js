var addMessage = function (id, className, mess, padding = 'bottom') {
    $(`#${id}`).addClass(className);
    $(`#${id}`).text(mess);
    $(`#${id}`).css(`padding-${padding}`, '1rem');
}

var removeMessage = function (id, className, padding = 'bottom', timeout = 5000) {
    setTimeout(function () {
        $(`#${id}`).removeClass(className);
        $(`#${id}`).text('');
        $(`#${id}`).css(`padding-${padding}`, '0rem');
    }, timeout);
}