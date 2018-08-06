$(function () {
    $("#submit-btn").click(function (event) {
        event.preventDefault()
        var telephone = $('input[name="telephone"]').val();
        var password = $('input[name="password"]').val();
        var remember = $('input[name="remember"]').checked ? 1:0;
        zlajax.post({
            'url': '/signin/',
            'data': {
                'telephone': telephone,
                'password': password,
                'remember': remember
            },
            'success': function (data) {
                if(data['code'] == 200){
                    var return_to = $("#return-to-span").text();
                    if(return_to){
                        window.location = return_to;
                    }else{
                        window.location = '/';
                    }
                }else{
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});