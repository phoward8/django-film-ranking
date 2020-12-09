promises = new Map();

$('div.film').each( async function() {

    var film = $(this);
    var id = film.attr('id');

    if (promises[id]) {
        console.log('awaiting ' + id);
        await promises[id];
    }

    promises[id] = new Promise ( async (resolve, reject) => {
        
        var api_response = localStorage.getItem(id);

        if (!api_response) {

            var settings = {
                "url": "https://imdb-api.com/en/API/Title/k_4075zegb/" + id,
                "method": "GET",
                "timeout": 0,
            };
            
            $.ajax(settings)
            .done(function (data, textStatus, jqXHR) {
                localStorage.setItem(id, JSON.stringify(data));
                updateHtml(film, data);
                resolve();
            })
            .fail(function (jqXHR, textStatus, errorThrown) {
                alert('API Failed to load for film ' + id +'. ' + errorThrown);
                reject();
            });
            
        } else {
            updateHtml(film, JSON.parse(api_response));
            resolve();
        }
    });

});

function updateHtml(film, response) {
    film.find('.title').text(response.title);
    film.find('.poster').attr('src', response.image);
}