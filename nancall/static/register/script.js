$(document).ready(function(){
    $('.sucess-validation').hide();
    $('.failed-validation').hide();
    var num = 1;
    $('#submit').click(function(e){
        e.preventDefault();
        num = num + 1;
        $('#myform').hide();
        if((num%2)==1){
            $('.sucess-validation').show();
            $('.formSpace').addClass('auto-size');
        }else{
            $('.sucess-validation').hide();
            $('.failed-validation').show();
            $('.formSpace').addClass('auto-size');

        }
    });
    $('.restaure').click(function(){
        $('.imageSpace').addClass('animated pulse');
        setInterval(function(){
            location.reload();
        },1000);
    });
    setInterval(function(){
        $('.imageSpace').addClass('animated bounce');
    },3000);
   
});