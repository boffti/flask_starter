$.noConflict();
jQuery(document).ready(function($) {

    $('.card-border').hover(function() {
        $(this).toggleClass('border border-danger');
    });

    $('#btn-json').on('click', function() {
        $.ajax({
            type: 'GET',
            url: '/getTrendingPostJson',
            success: function(data) {
                console.log(data);
                $("#box-json").text(data);
            }
        });
    });

});