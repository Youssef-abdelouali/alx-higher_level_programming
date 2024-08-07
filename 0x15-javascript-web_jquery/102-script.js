$(document).ready(function() {
    $('#btn_translate').click(function() {
        const languageCode = $('#language_code').val(); // Get the value from the input field
        $.ajax({
            url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
            method: 'GET',
            success: function(data) {
                $('#hello').text(data.hello); // Display the translated greeting
            },
            error: function() {
                $('#hello').text('Error fetching translation');
            }
        });
    });
});
