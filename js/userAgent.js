(function(){
2
    var ua = navigator.userAgent.toUpperCase();
3
    if(ua.indexOf('IPHONE') != -1 || (ua.indexOf('ANDROID') != -1 && ua.indexOf('MOBILE') != -1)){
4
        location.href = '/m/';
5
    }
6
}());
