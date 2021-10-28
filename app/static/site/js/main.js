//Home Page Slide
(function ($) {
    "use strict";

    $('.homepage-slides').owlCarousel({
        items: 1,
        dots: false,
        nav: true,
        loop: true,
        autoplay: true,
        autoplayTimeout: 5000,
        navText: ["<i class='la la-angle-left'></i>", "<i class='la la-angle-right'></i>"]
    });


    $(".homepage-slides").on("translate.owl.carousel", function () {
        $(".single-slide-item h1").removeClass("animated fadeInUp").css("opacity", "1");
        $(".single-slide-item h5").removeClass("animated fadeInDown").css("opacity", "1");
    });

    $(".homepage-slides").on("translated.owl.carousel", function () {
        $(".single-slide-item h1").addClass("animated fadeInUp").css("opacity", "1");
        $(".single-slide-item h5").addClass("animated fadeInDown").css("opacity", "1");
    });

// Logo Carousel

    $('.logo-carousel').owlCarousel({
        items: 5,
        margin: 30,
        dots: true,
        nav: false,
        loop: true,
        autoplay: true,
    });

// Mobile Menu

    $(".navbar-toggler").on("click", function () {
        $(this).toggleClass("active");
    });

    $(".navbar-nav li a").on("click", function () {
        $(".sub-nav-toggler").removeClass("active");
    });

    var subMenu = $(".navbar-nav .sub-menu");

    if (subMenu.length) {
        subMenu
            .parent("li")
            .children("a")
            .append(function () {
                return '<button class="sub-nav-toggler"> <i class="fa fa-angle-down"></i> </button>';
            });

        var subMenuToggler = $(".navbar-nav .sub-nav-toggler");

        subMenuToggler.on("click", function () {
            $(this).parent().parent().children(".sub-menu").slideToggle();
            return false;
        });
    }

//jQuery Sticky Area
    $('.sticky-area').sticky({
        topSpacing: 0,
    });



//Isotope Filter

    $('.port-menu li').on('click', function () {
        var selector = $(this).attr('data-filter');

        $('.port-menu li').removeClass("active");

        $(this).addClass("active");

        $(".portfolio-list").isotope({
            filter: selector,
            percentPosition: true,
        });

    });


//jQuery Animation
    new WOW().init(

    );

// Menu Active Color

    $(".main-menu .navbar-nav .nav-link").on("click", function () {
        $(".main-menu .navbar-nav .nav-link").removeClass("active");
        $(this).addClass("active");
    });

    jQuery(window).on("load", function () {
        jQuery(".site-preloader-wrap, .slide-preloader-wrap").fadeOut(1000);
    });

    $('#myCollapsible').collapse({
        toggle: false
    });

     $('.project-slider').owlCarousel({
         loop:true,
         nav:false,
         autoplay:true,
         autoplayHoverPause: true,
         mouseDrag: true,
         center: false,
         dots: true,
         smartSpeed:1500,
         margin: 20,
         responsive:{
            0:{
                items:1
            },
             576:{
                items:2
             },
             992:{
                items:2
             },
             1200:{
                items:2
            }
         }
    });


        // // Project Slider
		// $('.project-slider').owlCarousel({
		// 	loop:true,
		// 	nav:false,
		// 	autoplay:true,
		// 	autoplayHoverPause: true,
		// 	mouseDrag: true,
		// 	center: false,
		// 	dots: true,
		// 	smartSpeed:1500,
		// 	margin: 20,
		// 	responsive:{
		// 		0:{
		// 			items:1
		// 		},
		// 		576:{
		// 			items:3
		// 		},
		// 		992:{
		// 			items:3
		// 		},
		// 		1200:{
		// 			items:3
		// 		}
		// 	}
		// });

}(jQuery));



