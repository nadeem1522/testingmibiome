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
      let formData = new FormData(this);
      $.ajax({
          type: 'POST',
          url: '',
          data: formData,
          cache: false,
          contentType: false,
          processData: false,
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
                  $('#resume').val('');
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