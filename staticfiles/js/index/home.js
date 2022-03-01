function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

$(function() {
    $('.counter').counterUp({
        delay:20,
        time:2000
    });
});

$(document).ready(function() {
    let w = window.matchMedia('(max-width: 1024px)');
    if (w.matches) {
        $('#bg-video').html('<source src="/static/videos/mobile_screen.mp4" type="video/mp4">')
    } else {
        $('#bg-video').html('<source src="/static/videos/big_screen.mp4" type="video/mp4">')
    }
});

// var flashToastEle = document.querySelector('#flash-sale-toast');
// var flashToast = new bootstrap.Toast(flashToastEle);

// $(document).ready(async function() {
//     await sleep(5000);
//     flashToast.show();
// });