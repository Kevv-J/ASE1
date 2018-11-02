function menu_bar_on() {
    if (document.getElementById("menu_bar").style.display === "block") {
        document.getElementById("menu_bar").style.display = "none";
        document.getElementById("profile").style.display = "none";
    }
    if (document.getElementById("menu_bar").style.display === "none"){
        document.getElementById("menu_bar").style.display = "block";
        document.getElementById("profile").style.display = "block";
    }
}

function menu_bar_off() {
    document.getElementById("menu_bar").style.display = "none";
    document.getElementById("profile").style.display = "none";
}

function user_profile_animation_in() {
    document.getElementById("profile").style.opacity = "1";
}

function user_profile_animation_out() {
    document.getElementById("profile").style.opacity = "0.8";
}