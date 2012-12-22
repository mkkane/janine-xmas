$(function(){
  if ($('body.home').length > 0) {
    
  }

  // Make sure the canvas always takes up the whole window
  $(window).resize(function() { 
    set_canvas_dimensions();
  });
  set_canvas_dimensions();

});

var set_canvas_dimensions = function() {
  $('.canvas').css({
    'width': $(window).width(),
    'height': $(window).height()
  });
}
