$.get("https://ipinfo.io", function(response) {
    // console.log(response.country);
    console.log($('#coun_inp').val());
    country = $('#coun_inp').val();
    if (country !== undefined){
        $('#coun').html("Рекомендованные туры в <div onclick='goProfile();' id='c'>" + country + "</div>");
    }
    else $('#coun').html("Рекомендованные туры в <div onclick='goProfile();' id='c'>" + response.country + "</div>");

    }, "jsonp");

function goProfile() {

    $('#c').addClass('d-none');
    $('#inp').removeClass('d-none');
}
