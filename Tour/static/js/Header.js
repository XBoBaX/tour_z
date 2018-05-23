if (window.location.pathname !== '/') { $('#glav').removeClass('active');}
if (window.location.pathname.indexOf("visa") !== -1) { $('#glav, #tyri, #abAs, #vihod').removeClass('active'); $('#tyri').addClass('active');}
if (window.location.pathname.indexOf("my") !== -1) { $('#glav, #tyri, #abAs, #vihod').removeClass('active'); $('#vihod').addClass('active');}

    function active(objName) {
        // if (!($(objName).hasClass('active'))){
            $('#glav, #tyri, #abAs').removeClass('active');
            $(objName).addClass('active');
            if ($('#glav').hasClass('active')) window.location = '/';
            if ($('#tyri').hasClass('active')) window.location.href = '/visa/';
            if ($('#abAs').hasClass('active')) window.location.href = '/about/as';
        // }
    }

    function RegVh(objName) {
        if ($(objName).hasClass('vhodD')){
            if ($('#hod').hasClass('vhodD')){
                $('#hod').removeClass('vhodD');
                $('#reg').addClass('vhodD');
                $('#formReg').css({ display: 'none' });
                $('#formVhod').css({ display: 'block' });
            }
            else {
                $('#reg').removeClass('vhodD');
                $('#hod').addClass('vhodD');
                $('#formVhod').css({ display: 'none' });
                $('#formReg').css({ display: 'block' });
            }
        }
    }

    function anichange(objName, vhod){
        if ($(objName).css('display') == 'none' ) {
            $(objName).animate({height: 'show'}, 200);
            $(vhod).addClass('active');
        }
        else {
            $(objName).animate({height: 'hide'}, 200);
            $(vhod).removeClass('active');
        }
    }
    $(document).mouseup(function (e) {
        var container = $('#divId');
        if (container.has(e.target).length === 0){
            $(container).animate({height: 'hide'}, 200);
            $('#vhod').removeClass('active');
        }
    });
    $(document).mouseup(function (e) {
        var container = $('#divId2');
        if (container.has(e.target).length === 0){
            $(container).animate({height: 'hide'}, 200);
            $('#vihod').removeClass('active');
        }
    });
