function res(ind) {
    if (ind == 1) {
        $('.автобусом').removeClass('d-none');
        if ($('#avt').hasClass('res_active')) {
            $('#avt').removeClass('res_active');
            $('.самолетом').removeClass('d-none');
            $('.поездом').removeClass('d-none');
            return
        }
        $('#avt').addClass('res_active');
        $('#sam').removeClass('res_active');
        $('#jd').removeClass('res_active');
        $('.самолетом').addClass('d-none');
        $('.поездом').addClass('d-none');

    }
    else if (ind == 2) {
        $('.самолетом').removeClass('d-none');
        if ($('#sam').hasClass('res_active')) {
            $('#sam').removeClass('res_active');
            $('.автобусом').removeClass('d-none');
            $('.поездом').removeClass('d-none');
            return
        }
        $('#sam').addClass('res_active');
        $('#jd').removeClass('res_active');
        $('#avt').removeClass('res_active');
        $('.автобусом').addClass('d-none');
        $('.поездом').addClass('d-none');
    }
    else if (ind == 3) {
        $('.поездом').removeClass('d-none');
        if ($('#jd').hasClass('res_active')) {
            $('#jd').removeClass('res_active');
            $('.автобусом').removeClass('d-none');
            $('.самолетом').removeClass('d-none');
            return
        }
        $('#jd').addClass('res_active');
        $('#sam').removeClass('res_active');
        $('#avt').removeClass('res_active');
        $('.автобусом').addClass('d-none');
        $('.самолетом').addClass('d-none');
    }
}

price = sum_pr = total = pr_kol_vies = 0;
hotelName = otelH = "";
priceVis1 = day_ot = 0;
json2_exc = {};

function select(id) {
    idP = '#blur' + id;
    idB = '#Add' + id;
    id_p = '#pr' + id;
    id_tr = '#tr' + id;
    sum_1 = Number($(id_p).html());
    sum_2 = Number($(id_tr).html());
    now = $(idB).html();
    i = "#" + id;
    check = $(i).prop("checked");
    if (now === "Убрать") {
        $(idP).css('filter', 'blur(0px)');
        $(idB).html("Добавить");
        sum_pr -= sum_1;
        json2_exc[id] = '0';
        json2_exc['t' + id] = '0';
        if (check) sum_pr -= sum_2;
    }
    else {
        $(idP).css('filter', 'blur(2px)');
        $(idB).html("Убрать");
        sum_pr += sum_1;
        json2_exc[id] = '1';
        if (check) {
            json2_exc["t" + id] = '1';
            sum_pr += sum_2;
        }
    }
}

function excursions(str, day, total) {
    day_ot = day;
    otelH = str;
    price_H = $('#price_H').html();
    $("#spinner").css("display", "block");
    a = setTimeout('$("#spinner").css("display","none");', 8000);
    price_H = total;
    $.ajax({
        type: "GET",
        url: "/doc/form/get_check/",
        data: {'ot': ot_, 'kyd': kyd_, 'price': price_, 'price_H': price_H, 'kol': kolvo},
        cache: false,
        success: function (data) {
            $('.ht').remove();
            $('#forH').append(data);
            $("#spinner").css("display", "none");
            bil = "";
            i = 0;
            for (ch in json1) {
                if (i > 0) bil += ',';
                bil += " " + ch;
                i++;
            }
            $('#kolvo').html('Количество человек: ' + kolvo);
            $('#bilets').html('Билеты на места:' + bil);
            $('#bilets_price').html('Стоимость всех билетов: ' + sum + " грн");
            $('#exc_').html('Экскурсии и трансферы: 0');
            ot = $('#ot').html();
            $('#vis').addClass('d-none');
            priceVis1 = Number($('#priceVis').html());
            total = Number(sum) + Number(ot) + Number(sum_pr);
            $('#vsego').html('Всего: ' + total + " грн");
            jQuery(document).ready(function ($) {
                //Оканчательный чек
                $('.btnOl').click(function () {
                    $("#spinner").css("display", "block");
                    a = setTimeout('$("#spinner").css("display","none");', 8000);
                    $.ajax({
                        type: "GET",
                        url: "/doc/form/get_res/",
                        data: {
                            'ot': ot_,
                            'kyd': kyd_,
                            'price': price_,
                            'json_ticket': JSON.stringify(json1),
                            'json_exc': JSON.stringify(json2_exc),
                            'kolvo': kolvo,
                            'otel_n': otelH,
                            'day_ot': day_ot
                        },
                        cache: false,
                        success: function (data) {
                            $("#spinner").css("display", "none");
                            if (data === 'ok') {
                                document.location.href = "/my/tour/";
                            }
                            if (data == "no") {
                                $('#vhod').click();
                            }
                        }
                    });

                });


                $('.btnBl').click(function (e) {
                    str = "Экскурсии и трансферы: " + sum_pr + " грн";
                    $('#exc_').html(str);
                    total = Number(sum) + Number(ot) + Number(sum_pr);
                    $('#vsego').html('Всего: ' + total + " грн");
                });
                $('#kolViz').keyup(function () {
                    kol_vises = $('#kolViz').val();
                    total -= pr_kol_vies;
                    pr_kol_vies = kol_vises * priceVis1;
                    total += pr_kol_vies;
                    if (kol_vises == 0) {
                        $('#vis').addClass('d-none');
                        $('#btnOl').removeClass('disabled');
                    }
                    else {
                        $('#vis').removeClass('d-none');
                        ysp = $('.ysp').html();
                        if (ysp == "Вы успеете") {
                            $('#btnOl').removeClass('disabled');
                        }
                        else $('#btnOl').addClass('disabled');
                    }

                    $('#vsego').html('Всего: ' + total + " грн");
                });
                $('#kolViz').change(function () {
                    kol_vises = $('#kolViz').val();
                    total -= pr_kol_vies;
                    pr_kol_vies = kol_vises * priceVis1;
                    total += pr_kol_vies;
                    if (kol_vises == 0) {
                        $('#vis').addClass('d-none');
                        $('#btnOl').removeClass('disabled');
                    }
                    else {
                        $('#vis').removeClass('d-none');
                        ysp = $('.ysp').html();
                        if (ysp == "Вы успеете") {
                            $('#btnOl').removeClass('disabled');
                        }
                        else $('#btnOl').addClass('disabled');
                    }

                    $('#vsego').html('Всего: ' + total + " грн");
                })
            });

        }
    });
}

ot_ = kolvo = kyd_ = price_ = "";
sum = 0;
json1 = {};


function go_bilet(ot, kyd, price, ind) {
    json1 = {};
    total = sum = 0;
    $("#spinner").css("display", "block");
    a = setTimeout('$("#spinner").css("display","none");', 8000);
    price_ = price;
    ot_ = ot;
    kyd_ = kyd;
    $.ajax({
        type: "GET",
        url: "/doc/form/get_place/",
        data: {'ot': ot, 'kyd': kyd, 'price': price},
        cache: false,
        success: function (data) {
            if (ind === 1) {
                $('#t01').addClass('d-none');
                $('#t02').removeClass('d-none');
                $('#t03').removeClass('d-none');

                $('#soder').remove();
                $('#t1').append(data).addClass('select');
                $('#t2').removeClass('select');
                $('#t3').removeClass('select');
            }
            else if (ind === 2) {
                $('#t02').addClass('d-none');
                $('#t01').removeClass('d-none');
                $('#t03').removeClass('d-none');

                $('#soder').remove();
                $('#t2').append(data).addClass('select');
                $('#t1').removeClass('select');
                $('#t3').removeClass('select');
            }
            else if (ind === 3) {
                $('#t03').addClass('d-none');
                $('#t01').removeClass('d-none');
                $('#t02').removeClass('d-none');

                $('#soder').remove();
                $('#t3').append(data).addClass('select');
                $('#t1').removeClass('select');
                $('#t2').removeClass('select');
            }
            $('#spinner').css("display", "none");
            jQuery(document).ready(function ($) {
                prc1 = Number($('#prc1').html());
                prc2 = Number($('#prc2').html());
                kol1 = kol2 = sum = 0;
                $('.black').click(function (e) {
                        e = $(e.target);
                        if (e.hasClass('active')) return;
                        ob = Number($('#ob').html());
                        pl = Number($('#pl').html());
                        pr = $('#pr');
                        id = e.attr("id");
                        if (e.hasClass('box')) {
                            e.removeClass('box');
                            if (e.hasClass('blackP')) {
                                $('#pl').html(--kol1);
                                sum -= prc2;
                                json1[id] = 0;
                            }
                            else {
                                $('#ob').html(--kol2);
                                sum -= prc1;
                                json1[id] = 0;
                            }
                        }
                        else {
                            e.addClass('box');
                            if (e.hasClass('blackP')) {
                                $('#pl').html(++kol1);
                                sum += prc2;
                                json1[id] = 1;
                            }
                            else {
                                $('#ob').html(++kol2);
                                sum += prc1;
                                json1[id] = 1;
                            }
                        }
                        pr.html(sum)
                    }
                );
                $('.vibor').click(function (e) {
                    if (sum <= 0) {
                        $('#pr').css('color', 'red');
                        a = setTimeout('$("#pr").css("color","black"); ', 3000);
                        return;
                    }
                    kyd = $('#country2').val();
                    kolvo = kol1 + kol2;
                    day = $('#dayInTour').html();
                    $("#spinner").css("display", "block");
                    a = setTimeout('$("#spinner").css("display","none");', 5000);
                    $.ajax({
                        type: "GET",
                        url: "/doc/form/get_hotel/",
                        data: {'kyd': kyd_, 'kol': kolvo, 'day': day},
                        cache: false,
                        success: function (data) {
                            $('#bil_').remove();
                            $('#hed_').remove();
                            $('#forH').append(data);
                            $("#spinner").css("display", "none");

                        }
                    });


                });
            });
        }
    });
}
