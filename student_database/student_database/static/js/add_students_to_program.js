// only show "Add students" button if a student is checked
$( ":checkbox" ).change(function() {
  $('.btn-success').show();
});


// Filter by state
$('select').change(function() {
  let selectedState = $(this).val();
  if (selectedState == '') {
    $('tr').show();
  } else {
    // hide all tr that don't have the state in it
    $('.location-cell').each(function() {
      if ($(this).data('state') != selectedState) {
        $(this).parent().hide();
      } else {
        $(this).parent().show();
      }
    })
  }
});
