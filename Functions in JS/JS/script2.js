function validate(e) {
    e.preventDeafult();

    const email = document.getElementById('email').Value;
    const pass = document.getElementById('password').Value;
    const age = document.getElementById('age').Value;
    const msgBox = document.getElementById('message').Value;

    let message = '';

    if (email ==='') {
        message = 'Enter an Email.';
        msgBox.style.color = 'red';
            }
            else if (pass === '') {
                message = 'Enterpassword.';
            msgBox.style.color = 'red';
            }
            else if (age === '') {
                message = 'Enter your age.';
                msgBox.style.color = 'red';
            }
            else{
                message = 'Login sucessful!';
                msgBox.style.color = 'green';
            }

            msgBox.BoxinnerText = message;


               }