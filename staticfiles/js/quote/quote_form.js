$("select[name='service_choice']").on('change', '', function() {
    let value = $(this).val();
    $.each($("select[name='specific_service'] optgroup"), function() {
        $(this).css('display', 'none');
    })
    $("select[name='specific_service']").val('');
    if (value == 'DNA Sequencing') {
        $("select[name='specific_service'] optgroup[label='DNA Sequencing']").css('display', '');
    } else if (value == 'RNA Sequencing') {
        $("select[name='specific_service'] optgroup[label='RNA Sequencing']").css('display', '');
    } else if (value == 'Epigenetics') {
        $("select[name='specific_service'] optgroup[label='Epigenetics']").css('display', '');
    } else if (value == 'Microarray') {
        $("select[name='specific_service'] optgroup[label='Microarray']").css('display', '');
    } else if (value == '10X') {
        $("select[name='specific_service'] optgroup[label='10X']").css('display', '');
    } else if (value == 'Pacbio') {
        $("select[name='specific_service'] optgroup[label='Pacbio']").css('display', '');
    } else if (value == 'Metagenomics') {
        $("select[name='specific_service'] optgroup[label='Metagenomics']").css('display', '');
    } else if (value == 'Metatranscriptomics') {
        $("select[name='specific_service'] optgroup[label='Metatranscriptomics']").css('display', '');
    }
});

$("input[type='radio']").on('change', '', function() {
    let value = $(this).val();
    let specify = this.parentElement.parentElement.lastElementChild;
    console.log(specify.type)
    if (specify.type == 'text') {
        console.log('specify true')
        if (value == 'Others') {
            console.log('others true')
            specify.style.display = '';
            specify.required = true;
        } else {
            specify.style.display = 'none';
            specify.required = false;
            specify.value = '';
        }
    }
});

$('form').on('submit', '', function() {
    addMessage('query-message', 'success', 'Please wait...', 'bottom');
});