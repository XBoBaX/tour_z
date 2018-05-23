if (window.location.pathname.indexOf("visa") !== -1) {
    if ($('.v1').hasClass('active2'))
    $.ajax({
        type: "GET",
        url: "/visa/sh/",
        data: 'sh',
        cache: false,
        success: function(data){
            $('#visInfo').html(data);
        }
        });
}


$(document).mouseup(function (e) {
    var container = $('#list');
    if (container.has(e.target).length === 0) $(container).animate({height: 'hide'}, 200);
});

function VisaActive(objName) {
    if (!($(objName).hasClass('active2'))){
        $('.v1, .v2, .v3, .v4, .v5, .v6').removeClass('active2');
        $(objName).addClass('active2');
        var data = 'sh';
        if (objName === '.v1') data = 'sh';
        else if (objName === '.v2') data = 'SHA';
        else if (objName === '.v3') data = 'China';
        else if (objName === '.v4') data = 'Asia';
        else if (objName === '.v5') data = 'Avstraliya';
        else if (objName === '.v6') data = 'Great';
        $.ajax({
            type: "GET",
            url: "/visa/" + data,
            data: data,
            cache: false,
            success: function(data){
                $('#visInfo').html(data);
            }
        });
        // window.location.href = "/visa/sh/";
    }
}
function VisaAnichange(objName){
    if ($(objName).css('display') == 'none' ) $(objName).animate({height: 'show'}, 200);
        else $(objName).animate({height: 'hide'}, 200);
}