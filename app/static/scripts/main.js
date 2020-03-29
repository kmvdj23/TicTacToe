function toggleForm(element_id) {
  console.log('toggleForm() ' +element_id)
  var element = document.getElementById(element_id);
  if (element.style.display === 'none') {
    console.log("none");
    element.style.display = "block";
  } else {
    console.log("block");
    element.style.display = "none";
  }
};

function switchToggle(x_id, y_id) {
  console.log('CLICK');
  toggleForm(x_id);
  toggleForm(y_id);
};

$("document").ready(function() {

  $('#upl-display-pic-btn').on('click', function() {
    $('#display-pic-file-input').trigger('click');
  });

  $('#display-pic-file-input').change(
    function(){
      $(this).closest('form').submit();
    }
  );

  $('#upl-display-vid-btn').on('click', function() {
    $('#display-vid-file-input').trigger('click');
  });

  $('#display-vid-file-input').change(
    function(){
      $(this).closest('form').submit();
    }
  );

  $("#video-rating").rateYo({
    rating: {{video.rating}},
    readOnly: {% if current_user.is_authenticated and current_user.id == video.account_id %} false {% else %} true {% endif %},
    precision: 1,
    onSet: function(rating, instance) {
      var new_video_rating = $("<input>").attr('type', 'hidden').attr('name', 'new-video-rating').val(rating);
      $('#video-rate-form').append(new_video_rating);
      $('#video-rate-form').submit();
    }
  });

});