$("select[name='service_choice']").on('change', '', function() {
    let value = $(this).val();
    $.each($("select[name='specific_service'] optgroup"), function() {
        $(this).css('display', 'none');
    })
    $("select[name='specific_service']").val('');
    if (value == 'DNA Sequencing') {
        $("select[name='specific_service'] optgroup[label='DNA based Sequencing']").css('display', '');
    } else if (value == 'RNA Sequencing') {
        $("select[name='specific_service'] optgroup[label='RNA based Sequencing']").css('display', '');
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

$("#add-row").on('click', '', function() {
    let tableBody = document.querySelector("#sample-table tbody");
    tableBody.insertAdjacentHTML(
        'beforeend',
        `
        <tr>
            <td>${tableBody.children.length + 1}</td>
            <td><input type="text" class="table-input" name="sample_labelled" required></td>
            <td><input type="text" class="table-input" name="species" required></td>
            <td><input type="text" class="table-input" name="source" required></td>
            <td><input type="number" class="table-input" name="qubit" required step="0.01"></td>
            <td><input type="number" class="table-input" name="total_volume" step="0.01"></td>
            <td><input type="number" class="table-input" name="total_amount" step="0.01"></td>
            <td><input type="text" class="table-input" name="od_280"></td>
            <td><input type="text" class="table-input" name="od_230"></td>
            <td><input type="text" class="table-input" name="library_type" required></td>
            <td><input type="text" class="table-input" name="barcode" required></td>
            <td><input type="text" class="table-input" name="pcr_product_size"></td>
            <td><input type="text" class="table-input" name="gb_sample" required></td>
            <td><input type="text" class="table-input" name="remark"></td>
        </tr>
        `
    );
});

$("#remove-row").on('click', '', function() {
    let tableBody = document.querySelector("#sample-table tbody");
    if (tableBody.children.length > 1) {
        tableBody.lastElementChild.remove();
    }
});

$('form').on('submit', '', function() {
    addMessage('sample-message', 'success', 'Please wait...', 'bottom');
});

$("#data-delivery-add-repeat").on('click', '', function() {
    let checked = $(this).prop('checked');
    if (checked) {
        let value = $('input[name="invoice_address"]').val();
        $('input[name="data_del_add"]').val(value);
    } else {
        $('input[name="data_del_add"]').val('');
    }
});