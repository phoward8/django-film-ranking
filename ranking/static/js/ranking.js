$('div.film').each( function() {
	var film = $(this);
    var id = film.attr('id');
    
    var api_response = localStorage.getItem(id);

    if (!api_response) {

        var settings = {
            "url": "https://imdb-api.com/en/API/Title/k_4075zegb/" + id,
            "method": "GET",
            "timeout": 0,
        };

        $.ajax(settings).done(function (response) {
            api_response = response;
            localStorage.setItem(id, JSON.stringify(response));
        });
    } else {
        api_response = JSON.parse(api_response);
    }
        
    film.find('.title').text(api_response.title);
    film.find('.poster').attr('src', api_response.image);

});