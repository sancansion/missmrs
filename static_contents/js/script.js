$(function(){
	var $btn = $('.pagetop');
	var isHidden = true;

	$btn.hide();
	$(window).scroll(function () {
		if( $(this).scrollTop() > 550 ) {
			if( isHidden ) {
				$btn.stop(true,true).fadeIn();
				isHidden = false;
			}
		} else {
			if( !isHidden ) {
				$btn.stop(true,true).fadeOut();
				isHidden = true;
			}
		}
	});
});
//bxslider
$(function(){
	var displayWidth = 0;
	$(window).on('load', function(){
		var displayWidth = $(window).width();
		if(displayWidth > 639){
			$('.bxslider').bxSlider({
				slideWidth: 372,
				minSlides: 3,
				maxSlides: 3,
				moveSlides: 1,
				slideMargin: 0
			});
		}else{
			$('.bxslider').bxSlider({
				slideWidth: 372,
				minSlides: 2,
				maxSlides: 2,
				moveSlides: 1,
				slideMargin: 0
			});
		}
	});
});
//flexslider
$(window).load(function() {
	$('.flexslider').flexslider({
		animation: "slide",
		slideshowSpeed: "3000",
		prevText: "",
		nextText: "",
		directionNav: false
	});
});
/*
$(function(){
	$('.slider').slick({
		arrows: true,
		dots:false,
		accessibility:true,
		slidesToShow:5,
		slidesToScroll:1,
		autoplay:true,
		infinite: true,
		autoplaySpeed:2000,
		responsive:[
		{
			breakpoint: 1488,
			settings:{
				slidesToShow: 4
	  		}
		},
		{
			breakpoint: 1116,
			settings:{
				slidesToShow: 3
	  		}
		},
		{
			breakpoint: 744,
			settings:{
				slidesToShow: 2
	  		}
		},
		{
			breakpoint: 372,
			settings:{
				slidesToShow: 1
			}
		}
		]
	});
});
*/
$(function() {
	$("nav#menu-l").mmenu({
	});
});	
