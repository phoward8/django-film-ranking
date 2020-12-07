  
    var settings = {
        "url": "https://imdb-api.com/en/API/Title/k_1234567/{{ film.IMDB_id }}",
        "method": "GET",
        "timeout": 0,
    };
    
    $.ajax(settings).done(function (response) {
        console.log(response);
    }); 