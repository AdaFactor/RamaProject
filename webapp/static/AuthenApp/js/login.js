$(document).ready(() => {
    $("#forget-form").hide();

    $("#forget-pw").click(() => {
        $("#login-form").hide(() => {
            $("#forget-form").show();
        });
    });

    $("#cancel-pw").click(() => {
        $("#forget-form").hide(() => {
            $("#login-form").show();
        });
    });
});