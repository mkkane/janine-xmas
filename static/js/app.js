// Deal with ajax for email sending
$(function(){
  if ($('.tell-michael').length === 0) {
    return;
  }

  var $wrap = $('.tell-michael');
  var $form = $wrap.find('form');
  var $sending = $wrap.find('.sending-email');
  var $sent = $wrap.find('.sent-email');

  $form.submit(function() {
    // Make sure the page doesn't shrink when displaying the loader
    $wrap.css({'min-height' : $wrap.height() });

    $form.hide();
    $sending.show();

    $.post('/email', $form.serialize()).done(function() {
      $sending.hide();
      $sent.show();

      $wrap.css({'min-height' : 'auto' });
    });

    return false;
  })
});





// // Canvas for drawing
// $(function(){
//   // Make sure the canvas always takes up the whole window
//   $(window).resize(function() { 
//     set_canvas_dimensions();
//   });
//   set_canvas_dimensions();
// });

// var set_canvas_dimensions = function() {
//   $('.canvas').css({
//     'width': $(window).width(),
//     'height': $(window).height()
//   });
// }
