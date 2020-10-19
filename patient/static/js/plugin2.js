$(document).ready(function () {
    $('.show-form').click(function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type:'get',
            dataType:'json',
            beforeSend: function () {
                $('#modal-book').modal('show');
            },
            success: function (data) {
                $('#modal-book .modal-content').html(data.html_form);
            }
        });
    });
    $("#modal-book").on('submit', '.create-form', function () {
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data : form.serialize(),
            type:form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid){
                    console.log('data is save');
                }else {
                    $('#modal-book .modal-content').html(data.html_form);
                }
            }
        });
        return false;
    })
});
