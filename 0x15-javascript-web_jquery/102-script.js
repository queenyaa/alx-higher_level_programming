// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', function () {
    // Event listener for the Translate button click
    $('input#btn_translate').on('click', function () {
      // Get the language code from the input field
      const lang = $('input#language_code').val();
      
      // Fetch the translation using AJAX
      $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
        dataType: 'json',
        success: function (content) {
          // Update the content of the hello div with the translation
          $('div#hello').text(content.hello);
        }
      });
    });
  });
