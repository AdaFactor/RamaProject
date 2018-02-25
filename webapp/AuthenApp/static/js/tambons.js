$(document).ready(() => {
    // const urlTambons = "https://cdn.rawgit.com/AdaFactor/thai-tambons/f2b52554/tambons/json/th.json";
    const urlTambons = "https://cdn.rawgit.com/sirimainson/thai-tambons/36d842ca/tambons/json/th.json";
    
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
                    var korat = itemTambons[tambons].changwat_pid;
                    if (korat == "30") {
                        $("#id_area").append(
                            '<option value="'+ itemTambons[tambons].name +'"></option>'
                        );
                    }
                };
            });
        },
        error: (err) => {
            console.log(err)
        }
    });
});