$(document).ready(function() {
    // Access data from Flask
    const data = {{ data | tojson }};

    // Event handlers for scroll buttons
    $('.up-button').click(function() {
        // Scroll up logic using jQuery's scrollTop() method
        $('html, body').animate({ scrollTop: 0 }, 500);
    });

    $('.down-button').click(function() {
        // Scroll down logic using jQuery's scrollTop() method
        $('html, body').animate({ scrollTop: $(document).height() }, 500);
    });
});