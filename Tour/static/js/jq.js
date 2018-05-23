date = new Date();
date.setDate(date.getDate()+7);
now = date.getFullYear() + '-' + ('0' + (date.getMonth() + 1)).slice(-2) + '-' + ('0' + date.getDate()).slice(-2);
$('#vr_pr').val(now);

jQuery(document).ready(function ($) {
    $('#formVhod').submit(function (e) {
        e.preventDefault();
        var data = $(this).serialize();
        $.ajax({
            type: "POST",
            url: "/auth/login/",
            data: data,
            cache: false,
            success: function (data) {
                if (data == 'ok') {
                    location.reload();
                    // $('#ak').html(data);
                }
                else {
                    $('#error-login').html(data);
                }
            }
        });
    });
});

valF = "";
valT = "";

$('#doc').submit(function (e) {
    e.preventDefault();

    kol = 0;
    if (valT.length <= 1) {
        $('#inpVilet').addClass('errorIn');
        kol++;
    }
    if (valF.length <= 1) {
        $('#inpPrib').addClass('errorIn');
        kol++;
    }
    if (kol > 0) return;
    $("#spinner").css("display", "block");
    a = setTimeout('$("#spinner").css("display","none");', 12000);
    var data = $(this).serialize();
    $.ajax({
        type: "POST",
        url: "/doc/form/",
        data: data,
        cache: false,
        success: function (data) {
            $("#spinner").css("display", "none");
            if (data == 'ok') {
                alert("Виза не нужна");
            }
            else {
                $('#con_gl').html(data);


            }
        }
    });
});

first_or_last = cn1 = cn2 = cn3 = cn4 = "";

function showCit(str, where) {
    flag_g = "false";
    tct = $('#tct').val();
    if (where === 'rec') {
        if (str.length <= 1) return;
        $('#city3').animate({height: 'show'}, 200);
        flag_g = "true";
    }
    else if (str.length <= 1 && tct !== "true") {
        if (where === 'in')
            if ($('#city').css('display') !== 'none') {
                $('#city').animate({height: 'hide'}, 200);
                valT = "";
            }
            else if ($('#city2').css('display') !== 'none') {
                $('#city2').animate({height: 'hide'}, 200);
                valF = "";
            }
        return false;
    }
    if (where === 'in') {
        $('#city').animate({height: 'show'}, 200);
        first_or_last = "input"
    }
    else if (where === 'rec') {
        first_or_last = "rec"
    }
    else {
        $('#city2').animate({height: 'show'}, 200);
        first_or_last = "output"
    }
    var data = str;
    tct = $('#tct').val();
    vilet = $('#inpVilet').val();
    prib = $('#inpPrib').val();
    $.ajax({
        type: "GET",
        url: "/doc/in/",
        data: {
            'data': data,
            'its': flag_g,
            'tct': tct,
            'vilet': vilet,
            'prib': prib,
            'p': first_or_last,
            'kol': str.length,
            'val': valT
        },
        cache: false,
        success: function (data1) {
            if (data1) {
                // alert(JSON.stringify(data1));
                if (data1[0]['city'] !== "1" && data1[0]['city'] !== "2")
                    if (where === 'rec') {
                        $('#gor001').html(data1[0]['city']);
                        cn1 = data1[0]['county'];
                    }
                    else if (where === 'in') {
                        $('#gor1').html(data1[0]['city']);
                        cn1 = data1[0]['county'];
                    }
                    else {
                        $('#gor01').html(data1[0]['city']);
                        cn1 = data1[0]['county'];
                    }
                if (data1[1]['city'] !== "1" && data1[1]['city'] !== "2")
                    if (where === 'rec') {
                        $('#gor002').html(data1[1]['city']);
                        cn2 = data1[1]['county'];
                    }
                    else if (where === 'in') {
                        $('#gor2').html(data1[1]['city']);
                        cn2 = data1[1]['county'];
                    }
                    else {
                        $('#gor02').html(data1[1]['city']);
                        cn2 = data1[1]['county'];
                    }
                if (data1[2]['city'] !== "1" && data1[2]['city'] !== "2")
                    if (where === 'rec') {
                        $('#gor003').html(data1[2]['city']);
                        cn3 = data1[2]['county'];
                    }
                    else if (where === 'in') {
                        $('#gor3').html(data1[2]['city']);
                        cn3 = data1[2]['county'];
                    }
                    else {
                        $('#gor03').html(data1[2]['city']);
                        cn3 = data1[2]['county'];
                    }
                if (data1[3]['city'] !== "1" && data1[3]['city'] !== "2")
                    if (where === 'rec') {
                        $('#gor004').html(data1[3]['city']);
                        cn4 = data1[3]['county'];
                    }
                    else if (where === 'in') {
                        $('#gor4').html(data1[3]['city']);
                        cn4 = data1[3]['county'];
                    }
                    else {
                        $('#gor04').html(data1[3]['city']);
                        cn4 = data1[3]['county'];
                    }
            }
            else {
            }
        }
    });
}


function Select(objname, num, str) {
    if (str == "recom") {
        $('#city3').animate({height: 'hide'}, 200);
        $('#inp').val($(objname).html());
        $('#inp').addClass('d-none');
        valF = $(objname).html();
        $('#Kyda').addClass('d-md-block');
        if (num === "1") $('#coun_inp').val(cn1);
        else if (num === "2") $('#coun_inp').val(cn2);
        else if (num === "3") $('#coun_inp').val(cn3);
        else if (num === "4") $('#coun_inp').val(cn4);
        $('#c').html($('#coun_inp').val()).removeClass('d-none');
        var data = $('#coun_inp').val();
        $.ajax({
            type: "GET",
            url: "/doc/up/",
            data: {'data': data},
            cache: false,
            success: function (data) {
                if (data['ok'] === "ok")
                    location.reload();
                else {
                    $('#rekm').html(data['html']);
                    $('#coun').html("Рекомендованные туры в <div onclick='goProfile();' id='c'>" + data['cntr'] + "</div>");
                }
            }
        });
    }
    else if (str === "prib") {
        $('#city2').animate({height: 'hide'}, 200);
        $('#inpPrib').val($(objname).html());
        valF = $(objname).html();
        $('#Kyda').addClass('d-md-block');
        if (num === "1") $('#country2').val(cn1);
        else if (num === "2") $('#country2').val(cn2);
        else if (num === "3") $('#country2').val(cn3);
        else if (num === "4") $('#country2').val(cn4);
    }
    else {
        $('#city').animate({height: 'hide'}, 200);
        $('#inpVilet').val($(objname).html());
        valT = $(objname).html();
        $('#Otkyda').addClass('d-md-block');
        if (num === "1") $('#country').val(cn1);
        else if (num === "2") $('#country').val(cn2);
        else if (num === "3") $('#country').val(cn3);
        else if (num === "4") $('#country').val(cn4);

    }
}


$(document).mouseup(function (e) {
    var container = $('#city');
    if (container.has(e.target).length === 0) {
        $('#city').animate({height: 'hide'}, 200);
    }
});
$(document).mouseup(function (e) {
    var container = $('#city2');
    if (container.has(e.target).length === 0) {
        $('#city2').animate({height: 'hide'}, 200);
    }
});


$('#formReg').submit(function (e) {
    e.preventDefault();
    var data = $(this).serialize();
    $.ajax({
        type: "POST",
        url: "/auth/register/",
        data: data,
        cache: false,
        success: function (data) {
            if (data == 'ok') {
                window.location.href = '/my/account/';
            }
            else {
                $('#error-login2').html(data);
            }
        }
    });
});

function go_rec(vil, pr) {
    $("#spinner").css("display", "block");
    a = setTimeout('$("#spinner").css("display","none");', 5000);
    $.ajax({
        type: "GET",
        url: "/doc/form/",
        data: {'vilet': vil, 'pr': pr, 'rec': 'true'},
        cache: false,
        success: function (data) {
            $('#res').html(data);
            var top = $('#res').offset().top - 60;
            $('body,html').animate({scrollTop: top}, 1000);
            $("#spinner").css("display", "none");
            if (data == "non") alert("error");
            if (data == 'ok') {alert("Виза не нужна");}
        }
    });
}


$('#bil').submit(function (e) {
    e.preventDefault();
    kol = 0;
    if (valT.length <= 1) {
        $('#inpVilet').addClass('errorIn');
        kol++;
    }
    if (valF.length <= 1) {
        $('#inpPrib').addClass('errorIn');
        kol++;
    }
    if (kol > 0) return;
    $("#spinner").css("display", "block");
    a = setTimeout('$("#spinner").css("display","none");', 5000);
    var data = $(this).serialize();
    $.ajax({
        type: "POST",
        url: "/doc/form/",
        data: data,
        cache: false,
        success: function (data) {
            // alert(data);
            $('#res').html(data);
            var top = $('#res').offset().top - 60;
            $('body,html').animate({scrollTop: top}, 1000);
            $("#spinner").css("display", "none");
            if (data == "non") alert("error");
            if (data == 'ok') {
                alert("Виза не нужна");
            }
        }
    });
});
