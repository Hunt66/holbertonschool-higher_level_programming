// lists all movies title by using the url
// https://swapi.co/api/films/?format=json
$.get('https://swapi.co/api/films/?format=json', function (stf, stat) {
  if (stat === 'success') {
    itms = stf.results;
    for (let i in itms) {
      $('#list_movies').append('<li>' + itms[i].title + '</li>');
    }
  }
});
