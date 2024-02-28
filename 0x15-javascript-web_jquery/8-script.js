const moviesUri = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
');

$.ajax({
  url: moviesUri,
  dataType: 'json'
}).done((data) => {
  const movies = data.results;

  for (let i = 0; i < movies.length; ++i) {
    const movieTitle = movies[i].title;
    const element = `<li>${movieTitle}`;
    $movieList.append(element);
  }
});
