$(document).ready(() => {
    const urlProvince = "https://cdn.rawgit.com/AdaFactor/thai-tambons/f2b52554/changwats/json/th.json";
    const urlAmphoes = "https://cdn.rawgit.com/AdaFactor/thai-tambons/f2b52554/amphoes/json/th.json";

    $.ajax({
        url: urlProvince,
        type: "GET",
        dataType: "json",
        async: true,
        crossDomain: true,
        success: (dataProvince) => {
            $.each(dataProvince.th, (indexProvince, itemProvince) => {
                itemProvince.sort((a, b) => { 
                    var provinceA = a.name.toUpperCase();
                    var provinceB = b.name.toUpperCase();
                    if(provinceA < provinceB){ return -1 };
                    if(provinceA > provinceB){ return 1 };
                    return 0;
                });
                for(var province = 0; province <= itemProvince.length; province++) {
                    if (itemProvince[province].name == "นครราชสีมา"){
                        $("#id_province").append(
                            '<option value="'+ itemProvince[province].name +'"></option>'
                        );
                                                        
                    }                           
                }
            });
        },
        error: (err) => {
            console.log(err)
        }
    });
});
