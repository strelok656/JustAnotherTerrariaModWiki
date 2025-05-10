$('#login-button').click(function() 
{
    const username = $('#username').val();
    const password = $('#password').val();
    const csrf = $('[name=csrfmiddlewaretoken]').val();
    const loginButton = $(this);

    if(!username) 
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

$('#create-account-button').click(function()
{
    const username = $('#username').val()
    const password = $('#password').val()
    const name = $('#name').val()
    const last_name = $('#last-name').val()
    const email = $('#email').val()
    const csrf = $('[name=csrfmiddlewaretoken]').val();

    if (!username)
    {
        alert("Пожалуйста, введите имя пользователя")
        return
    }
    else if(!password)
    {
        alert("Пожалуйста, введите пароль")
        return
    }
    else if (!email)
    {
        alert("Пожалуйста, введите электронную почту")
        return
    }

    $.ajax(
    {
        url: '/registration/',
        type: 'POST',
        data:
        {
            'username': username,
            'password': password,
            'name': name,
            'last_name': last_name,
            'email': email,
            'csrfmiddlewaretoken': csrf
        },
        dataType: 'json',

        success: function(data)
        {
            console.log('Success: ', data)
        },

        error: function(error)
        {
            console.log('Error: ', error)
        }
    })
})