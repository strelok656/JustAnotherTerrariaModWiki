$("#button-submit").click(function() 
{
    const email = $("#email").val();
    const csrf = $('[name=csrfmiddlewaretoken]').val();
    const submitButton = $(this);

    if(!email) 
    {
        alert('Пожалуйста, введите email');
        return;
    }

    $.ajax({
        url: '/feedback/',
        type: 'POST',
        data: 
        {
            'email': email,
            'csrfmiddlewaretoken': csrf
        },
        dataType: 'json',

        success: function(data) {
            console.log('Успех! ', data);
            submitButton.text('Отправлено');
            submitButton.prop('disabled', true);
            submitButton.css
            ({
                'background-color': '#4CAF50',
                'color': '#fff',
            });
        },

        error: function(error) {
            console.error('Ошибка: ', error);
            submitButton.text('Не удалось отправить!');
            submitButton.prop('disabled', false);
            submitButton.css
            ({
                'background-color': 'red',
                'color': 'fff'
            })
        }
    })
});

$('#login-button').click(function() 
{
    const login = $('#username').val();
    const password = $('#password').val();
    const csrf = $('[name=csrfmiddlewaretoken]').val();
    const loginButton = $(this);

    if(!login) 
    {
        alert('Пожалуйста, введите логин');
        return;
    }

    $.ajax({
        url: '/account/',
        type: 'POST',
        data: 
        {
            'username': username,
            'password': password,
            'csrfmiddlewaretoken': csrf
        },
        dataType: 'json',

        success: function(data) {
            console.log('Успех! ', data);
            loginButton.text('Отправлено');
            loginButton.prop('disabled', true);
            loginButton.css
            ({
                'background-color': '#4CAF50',
                'color': '#fff',
            });
        },

        error: function(error) {
            console.error('Ошибка: ', error);
            loginButton.text('Не удалось отправить!');
            loginButton.prop('disabled', false);
            loginButton.css
            ({
                'background-color': 'red',
                'color': 'fff'
            })
        }
    })
})