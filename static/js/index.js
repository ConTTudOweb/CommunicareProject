Index = {
  init: function(){

    // Remodal auto load

    $(function(){
        const hash = window.location.hash;
        if (hash == "") {
            var inst = $.remodal.lookup[$('[data-remodal-id=modal]').data('remodal')];
            inst.open();
        }
    });

  }
};

$(document).ready(function() {
  Index.init();
});