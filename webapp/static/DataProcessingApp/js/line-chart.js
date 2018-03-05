$(document).ready(()=>{
    var dataPoints = [];

    var options =  {
        animationEnabled: true,
        theme: "light1",
        title: {
            text: "สรุปยอดสมาชิกในแต่ละอำเภอ"
        },
        axisX: {
            title: "อำเภอ",
        },
        axisY: {
            title: "จำนวนสมาชิก",
            titleFontSize: 24,
            suffix: "คน",
        },
        data: [{
            type: "line",
            cursor: "pointer",
            color: "#359dbb",
            yValueFormatString: "### คน", 
            dataPoints: dataPoints
        }]
    };

    function addArea(data) {
        for (var i = 0; i < data.length; i++) {
            dataPoints.push({
                label: data[i].name,
                y: data[i].amount
            });         
        }
        $("#chartLine").CanvasJSChart(options);

    }

    $.getJSON("/static/json/area_data.json", addArea);
});