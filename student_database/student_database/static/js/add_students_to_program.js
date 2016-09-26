// only show "Add students" button if a student is checked
$( ":checkbox" ).change(function() {
  $('.btn-success').show();
});


const filterStates = function(state) {
  if (state == '') {
    $('tr').show();
  } else {
    // hide all tr that don't have the state in it
    $('tr').each(function() {
      if ($(this).data('state') != state) {
        $(this).hide();
      } else {
        $(this).show();
      }
    })
  }
}

$('select').change(function() {
  let selectedState = $(this).val();
  $('#searchTextbox').val('')
  filterStates(selectedState);
});


// fuzzy search for student names
const names = $('.names')
const namesObj = names.toArray().map(function(obj) {
    return {'n' : obj.innerHTML, 'id': $(obj).parent().data('pk') };
  })
const fuseOptions = {
    caseSensitive: false,
    includeScore: false,
    shouldSort: true,
    tokenize: false,
    threshold: 0.6,
    location: 0,
    distance: 100,
    maxPatternLength: 32,
    keys: ["n"]
};
var fuse = new Fuse(namesObj, fuseOptions);

$('#searchTextbox').keyup(function () {
    if ($(this).val().length == 0) {
      $('tr').show();
      filterStates($('select').val())
    } else {
      var results = fuse.search($('#searchTextbox').val());
      ids = results.map(function(obj) { return obj.id; })
      $('tbody tr').each(function() {
        let tableRow = $(this);
        if (!$.inArray(tableRow.data('pk'), ids) &&
            (!$('select').val() ||
             $('select').val() == tableRow.data('state'))) {
          tableRow.show();
        } else {
          tableRow.hide();
        }
      })
    }
});