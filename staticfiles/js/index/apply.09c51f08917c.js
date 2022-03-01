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

$("#intern-form").on('submit', '', function (event) {
  event.preventDefault();
  if (!enquirySent) {
      enquirySent = true;
      addMessage('intern-message', '', 'Please wait...');
      let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
      let name = $('input[name="name"]').val();
      let email = $('input[name="email"]').val();
      let phone = $('input[name="phone"]').val();
      let education = $('input[name="education"]').val();
      let stream = $('input[name="stream"]').val();
      let duration = $('input[name="duration"]').val();
      $.ajax({
          type: 'POST',
          url: '',
          data: {
              'csrfmiddlewaretoken': csrfToken,
              'name': name,
              'email': email,
              'phone': phone,
              'education': education,
              'stream': stream,
              'duration': duration,
          },
          success: function (response) {
              if (response.status) {
                  addMessage('intern-message', 'success', response.message);
                  removeMessage('intern-message', 'success');
                  $('input[name="name"]').val('');
                  $('input[name="email"]').val('');
                  $('input[name="phone"]').val('');
                  $('input[name="education"]').val('');
                  $('input[name="stream"]').val('');
                  $('input[name="duration"]').val('');
              } else {
                  addMessage('intern-message', 'error', response.message);
                  removeMessage('intern-message', 'error');
              }
              enquirySent = false;
          },
          error: function (_) {
              addMessage('intern-message', 'error', 'Internal Server Error');
              removeMessage('intern-message', 'error');
              enquirySent = false;
          }
      });
  }
});