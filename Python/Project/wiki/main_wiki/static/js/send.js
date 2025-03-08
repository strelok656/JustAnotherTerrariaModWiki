 $("#button-submit").click(function() {
    const email = $("#email").val();
    const csrf = $('[name=csrfmiddlewaretoken]').val();
    let jsonString = JSON.stringify({email, csrf});
    $.ajax({
        url: '/feedback/',
        type: 'POST',
        data: jsonString,
        dataType: 'json',
        success: function(data) {
            console.log('Успех! ', data);
        },
        error: function(error) {
            console.error('Ошибка: ', error);
        },
    })
});