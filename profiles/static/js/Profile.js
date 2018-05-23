$.get("https://ipinfo.io", function(response) {
    $('#con').val(response.country);
    console.log(response.country);
}, "jsonp");

function editClick() {
     if (!($('#edit').hasClass('d-none'))){
         $('.d-none').removeClass('d-none');
         $('.ot').addClass('d-none');
         $('#vihod').addClass('active')
     }
     else {
         $('.d-none').removeClass('d-none');
         $('.in').addClass('d-none');
         $('#vihod').addClass('active')

     }
}

$('#edit1').submit(function(e){
        e.preventDefault();
        var data = $(this).serialize();
        $.ajax({
            type: "POST",
            url: "/my/account/edit/",
            data: data,
            cache: false,
            success: function(data){
                if (data == 'ok'){
                    location.reload();
                }
                else{
                   $('#error-login2').html(data);
                }
            }
        });
     });