$(document).ready(function() {
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
        let moviesList = $('#list_movies');
        data.results.forEach(function(movie) {
            moviesList.append('<li>' + movie.title + '</li>');
        });
    });
});
