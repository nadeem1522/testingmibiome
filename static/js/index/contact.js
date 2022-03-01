const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});

var enquirySent = false;

$("#contact-form").on('submit', '', function (event) {
  event.preventDefault();
  if (!enquirySent) {
      enquirySent = true;
      addMessage('contact-message', '', 'Please wait...');
      let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
      let name = $('input[name="name"]').val();
      let email = $('input[name="email"]').val();
      let message = $('textarea[name="message"]').val();
      let phone = $('input[name="phone"]').val();
      $.ajax({
          type: 'POST',
          url: '',
          data: {
              'csrfmiddlewaretoken': csrfToken,
              'name': name,
              'email': email,
              'phone': phone,
              'message': message,
          },
          success: function (response) {
              if (response.status) {
                  addMessage('contact-message', 'success', response.message);
                  removeMessage('contact-message', 'success');
                  $('input[name="name"]').val('');
                  $('input[name="email"]').val('');
                  $('input[name="message"]').val('');
                  $('input[name="phone"]').val('');
              } else {
                  addMessage('contact-message', 'error', response.message);
                  removeMessage('contact-message', 'error');
              }
              enquirySent = false;
          },
          error: function (_) {
              addMessage('contact-message', 'error', 'Internal Server Error');
              removeMessage('contact-message', 'error');
              enquirySent = false;
          }
      });
  }
});