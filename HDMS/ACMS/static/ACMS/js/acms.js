/**
 * Created by koyexes on 8/4/2016.
 */

$('#loginModalJs').modal('show');// automatically showing the modal login error when a login error occurs

$('#loginModalJs').on('hidden.bs.modal', function(e){
    $('#loginErrorAlert').alert('close');
    $('#loginModalJs').attr('id', 'loginModal');
});

$('.iconLabel').mouseenter(function(e){
    /*var element = e.target();
    alert(element);
   element.siblings('.icon')[0].css({" -ms-filter" :"grayscale(0%)", "filter" : "grayscale(0%)", "-webkit-filter" : "grayscale(0%)"});*/
});

$('.iconLabel').mouseleave(function(e){
   $('.iconLabel').siblings('img').css({" -ms-filter" :"grayscale(100%)", "filter" : "grayscale(100%)", "-webkit-filter" : "grayscale(100%)"});
});