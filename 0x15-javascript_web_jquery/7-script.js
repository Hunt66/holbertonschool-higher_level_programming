// fetche and replaces the name of the url
// https://swapi.co/api/people/5/?format=json
$.get('https://swapi.co/api/people/5/?format=json', function (stf, stat) {
  if (stat === 'success') {
    $('#character').text(stf.name);
  }
});
