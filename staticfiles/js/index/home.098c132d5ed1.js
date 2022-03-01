function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

$(document).ready(async function () {
    const mainDiv = document.querySelector('.hero-content-change');
    const largeText = ['We Are Control Freaks', 'Know Your Microbes','Genomics For All', 'Science Is Art', 'Growing Together ...Molecule By Molecue', 'Coding To Decode Life','Full Fledged Genomics Co.', 'Only Genomics Lab In Mumbai'];
    let counter = 0;
    while(true) {
        mainDiv.innerHTML = `
            <div>
                <h1 class = "hero-lg-text">
                    ${largeText[counter%6]}
                </h1>
            </div>
        `;
        switch(counter%6) {
            case 0:
                await sleep(2620);
                break
            case 1:
                await sleep(3350);
                break
            case 2:
                await sleep(4200);
                break
            case 3:
                await sleep(3000);
                break
            case 4:
                await sleep(10450);
                break
            case 5:
                await sleep(6050);
                break
        }
        counter += 1;
    }
});

$(function() {
    $('.counter').counterUp({
        delay:20,
        time:2000
    });
});