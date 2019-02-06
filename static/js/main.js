Main = {
  init: function(){


    // Mobile menu

    $(".menu-trigger").click(function(e) {
      $("header nav").toggle();
      e.stopPropagation();
    });


    // ScrollReveal

    ScrollReveal().reveal(".cards-list li",{ distance: "-100px", duration: 2000 })
    ScrollReveal().reveal(".big-button",{ duration: 900 })
    ScrollReveal().reveal(".calendar li",{ distance: "-100px", duration: 2000 })
    ScrollReveal().reveal("footer img",{ delay: 200, duration: 2000 })


    // FlexSlider

    $('.flexslider').flexslider({
      randomize: true,
      startAt: 0,
      slideshow: true,
      initDelay: 0,
      touch: true
    });


    // Remodal auto load

    // $(function(){
    //     var inst = $.remodal.lookup[$('[data-remodal-id=modal]').data('remodal')];
    //     inst.open();
    // });


    // Scroll links

    $('a[href^="#"]').on('click',function (e) {
        e.preventDefault();
        var self = $(this);
        var target = this.hash;
        $target = $(target);
        $('html, body').stop().animate({
            'scrollTop':  $target.offset().top + 2
        }, 1000, function () {
          window.location.hash = target;
          $('a[href^="#"]').removeClass('on-section');
          self.addClass('on-section');
        });
    });

  }
}

$(document).ready(function() {
  Main.init();
});
