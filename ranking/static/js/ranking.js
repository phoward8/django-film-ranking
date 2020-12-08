$('div.film').each( function() {
	var film = $(this);
	var id = film.attr('id');
		
    var settings = {
        "url": "https://imdb-api.com/en/API/Title/k_4075zegb/" + id,
        "method": "GET",
        "timeout": 0,
    };
	
    $.ajax(settings).done(function (response) {
        film.find('.title').text(response.title);
        film.find('.poster').attr('src', response.image);
    });

});