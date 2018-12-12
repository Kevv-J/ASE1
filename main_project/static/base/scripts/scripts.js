function menu_bar_on() {
    document.getElementById("menu_bar").style.display = "block";
    document.getElementById("profile").style.display = "block";
    document.getElementById("page_overlay_2").style.display = "block";
}

function menu_bar_off() {
    document.getElementById("menu_bar").style.display = "none";
    document.getElementById("profile").style.display = "none";
    document.getElementById("page_overlay_2").style.display = "none";
}

function nav_bar_background() {
    if (document.body.scrollTop > 650 || document.documentElement.scrollTop > 650) {
        document.getElementById("nav_bar").style.backgroundColor = '#008B8B';
        document.getElementById("nav_bar").style.borderBottom = 'none';
    } else {
        document.getElementById("nav_bar").style.background = 'transparent';
        document.getElementById("nav_bar").style.borderBottom = '0.5px solid dimgray';
    }
}

/*======================================Back to top function =============================*/
function scrollFunction() {
    if (document.body.scrollTop > 65 || document.documentElement.scrollTop > 65) {
        document.getElementById("back_to_top").style.display = "block";
    } else {
        document.getElementById("back_to_top").style.display = "none";
    }
}

function scrolltopFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

/*=====================================Google map===========================================*/

function stop_scrolling() {
    $("body").css({overflow: 'hidden'});
}

function start_scrolling() {
    $("body").css({overflow: 'visible'});
}


/*====================================Copy to clipboard===================================*/

function copy_to_clipboard() {
    if (document.getElementById('copy_to_clipboard_btn').innerText == 'Copy to clipboard') {
        var copyText = document.getElementById("co-ords");
        copyText.select();
        document.execCommand("copy");
        document.getElementById('copy_to_clipboard').innerText = 'assignment_turned_in';
        document.getElementById('copy_to_clipboard_btn').innerText = 'copied';
        alert("Copied the text: " + copyText.value + '\n\n' + 'Paste the co-ords in google maps search bar to get the route from your place');
        setTimeout(change_icon_to_normal, 5000);
    }
}

function change_icon_to_normal() {
    document.getElementById('copy_to_clipboard').innerText = 'file_copy';
    document.getElementById('copy_to_clipboard_btn').innerText = 'Copy to clipboard';
}

/*========================================================================================*/
/*function display_evoting_txt() {
    document.getElementById("evoting").style.display = "block";
}

function remove_evoting_txt() {
    document.getElementById("evoting").style.display = "none";
}
*/
/*function user_profile_animation_in() {
    document.getElementById("profile").style.opacity = "1";
}

function user_profile_animation_out() {
    document.getElementById("profile").style.opacity = "0.8";
}*/

/*===============================Loading Bar=======================================*/
var loading_percent = 5;
var loading_bar_inc = 5;
var time_interval = 100;

function load() {
    $('#loading').animate({width: loading_percent + '%'}, 0);
    loading_percent += loading_bar_inc;
    if (loading_percent <= 100) {
        if ($(document).ready()){
            loading_bar_inc = 5;
            time_interval = 10;
        }
        setTimeout(load, time_interval);
    }
    else {
        loading_bar_inc /= 1.2;
        start_scrolling();
        document.getElementById('loading').style.display = 'none';
    }
}
