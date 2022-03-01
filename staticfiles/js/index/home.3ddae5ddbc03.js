function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

$(function() {
    $('.counter').counterUp({
        delay:20,
        time:2000
    });
});

// var flashToastEle = document.querySelector('#flash-sale-toast');
// var flashToast = new bootstrap.Toast(flashToastEle);

// $(document).ready(async function() {
//     await sleep(5000);
//     flashToast.show();
// });