$('select[name="dna_source"]').on('change', '', function() {
    let value = $(this).val();
    if (value == 'Others') {
        $('#dna-source-others-card').css('display', '');
        $('#dna-source-others').prop('required', true);
    } else {
        $('#dna-source-others-card').css('display', 'none');
        $('#dna-source-others').prop('required', false);
        $('#dna-source-others').val('');
    }
});

var requestSent = false;

$('form#apply-form').on('submit', '', function(event) {
    if (!requestSent) {
        event.preventDefault();
        requestSent = true;
        let title = $('#title').val().trim();
        let description = $('#description').val().trim();
        let nature_of_experiment = $('#nature-of-experiment').val().trim();
        let dna_source = $('#dna-source').val().trim();
        let dna_source_others = '';
        if (dna_source == 'Others') {
            dna_source_others = $('#dna-source-others').val().trim();
        }
        let csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
        $('.spinner-border').css('display', '');
        $.ajax({
            type: 'POST',
            url: '/grants/apply/',
            data: {
                'title': title,
                'description': description,
                'nature_of_experiment': nature_of_experiment,
                'dna_source': dna_source,
                'dna_source_others': dna_source_others,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(response) {
                if (response.status) {
                    $('#title').val('');
                    $('#description').val('');
                    $('#nature-of-experiment').val('');
                    $('#dna-source').val('');
                    $('#dna-source-others').val('');
                    $('#terms-and-conditions').prop('checked', false);
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