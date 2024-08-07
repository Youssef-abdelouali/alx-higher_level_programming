$(document).ready(function() {
    function fetchGreeting() {
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
    }

    // Click event for the "Translate" button
    $('#btn_translate').click(fetchGreeting);

    // Keypress event for the input field
    $('#language_code').keypress(function(event) {
        if (event.which === 13) { // Enter key code
            fetchGreeting();
        }
    });
});
