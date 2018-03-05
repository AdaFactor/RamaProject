$(document).ready(() => {
    const urlAmphoes = "https://cdn.rawgit.com/AdaFactor/thai-tambons/f2b52554/amphoes/json/th.json";
    
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
                    var korat = itemAmphoes[amphoes].changwat_pid;
                    if (korat == "30") {
                        $("#id_subarea").append(
                            '<option value="'+ itemAmphoes[amphoes].name +'"></option>'
                        );
                    }
                };
            });
        },
        error: (err) => {
            console.log(err)
        }
    });
})