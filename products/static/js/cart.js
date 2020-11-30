function muteMessage() {
  $('#message').css('visibility', 'hidden');
}
$(document).ready(function() {
  $('#thecart').fadeOut();
  $('#cart-icon').hover(function() {
    $(this).css('cursor', 'pointer');
  });
  $('#cart-icon').click(function() {
    $('#thecart').css('visibility', 'visible');
    $('#thecart').slideToggle(1000);
  });
  $('#close-modal-btn').click(function() {
    $('#thecart').slideToggle(1000);
  });
  $('#close-modal-x').click(function() {
    $('#thecart').slideToggle(1000);
  });
});
