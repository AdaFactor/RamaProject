$(document).ready(() => {
    // const urlAmphoes = "/static/json/subarea.json";    
    // const urlTambons = "/static/json/area.json";
    const urlAmphoes = "https://cdn.rawgit.com/AdaFactor/thai-tambons/f2b52554/amphoes/json/th.json";    
    const urlTambons = "https://cdn.rawgit.com/sirimainson/thai-tambons/4aaaec95/tambons/json/th.json";

    $.ajax({
        url: urlAmphoes,
        type: "GET",
        dataType: "json",
        async: true,
        crossDomain: true,
        success: (dataAmphoes) => {
            $.each(dataAmphoes.th, (indexAmphoes, itemAmphoes) => {
                itemAmphoes.sort((a, b) => { 
                    var amphoesA = a.name.toUpperCase();
                    var amphoesB = b.name.toUpperCase();
                    if(amphoesA < amphoesB){ return -1 };
                    if(amphoesA > amphoesB){ return 1 };
                    return 0;
                });
                for(var amphoes = 0; amphoes <= itemAmphoes.length; amphoes++){
                    if(itemAmphoes[amphoes].changwat_pid == "30") {
                        $("#id_subarea").append(
                            '<option value="'+ itemAmphoes[amphoes].pid +'">'+ itemAmphoes[amphoes].name +'</option>'
                        );
                    };
                };
            });
        },
        error: (err) => {
            console.log(err)
        }
    });

    $("#id_subarea").change(() => {
        var subarea = $("#id_subarea").val();
        console.log(subarea);
        $("#id_area").empty();
        $.ajax({
            url: urlTambons,
            type: "GET",
            dataType: "json",
            async: true,
            crossDomain: true,
            success: (dataTambons) => {
                $.each(dataTambons.th, (indexTambons, itemTambons) => {
                    itemTambons.sort((a, b) => { 
                        var nameA = a.name.toUpperCase();
                        var nameB = b.name.toUpperCase();
                        if(nameA < nameB){ return -1 };
                        if(nameA > nameB){ return 1 };
                        return 0;
                    });
                    for(var tambons = 0; tambons <= itemTambons.length; tambons++){
                        if(subarea == itemTambons[tambons].amphoe_pid){
                            $("#id_area").append(
                                '<option value="'+ itemTambons[tambons].pid +'">'+ itemTambons[tambons].name +'</option>'
                            );
                        };
                    };
                });
            },
            error: (err) => {
                console.log(err)
            }
        });
    });
});