function animate_nav_bar() {
    var scrollHeight = document.body.scrollHeight;
    if (scrollHeight <= 500){
        document.getElementById('nav_bar').style.display = 'none';
    }
    else {
        document.getElementById('nav_bar').style.display = 'flex';
    }
}

function animate_menu_bar() {
    var scrollHeight = document.body.scrollHeight;
    if (scrollHeight <= 500){
        document.getElementById('menu_bar_display_open').style.display = 'none';
    }
    else {
        document.getElementById('menu_bar_display_open').style.display = 'block';
    }
}

function expand_organiser() {
    if (document.getElementById('login_container').style.height == '470px') {
        document.getElementById('organiser_div').classList.remove('col');
        document.getElementById('organiser_div').classList.add('col-9');
        document.getElementById('voter_div').classList.remove('col');
        document.getElementById('voter_div').classList.add('col-3');
        document.getElementById('org_icn').style.backgroundColor = '#008B8B';
        document.getElementById('org_icn').style.cursor = 'default';
        document.getElementById('organiser_link_align').style.cssFloat = 'left';
        document.getElementById('org_desc').style.display = 'block';
        document.getElementById('organiser').style.display = 'none';
        document.getElementById('organiser_link').style.display = 'block';
    }
}

function contract_organiser() {
    document.getElementById('organiser_div').classList.remove('col-9');
    document.getElementById('organiser_div').classList.add('col');
    document.getElementById('voter_div').classList.remove('col-3');
    document.getElementById('voter_div').classList.add('col');
    document.getElementById('org_icn').style.background = 'none';
    document.getElementById('org_icn').style.cursor = 'default';
    document.getElementById('organiser_link_align').style.cssFloat = 'none';
    document.getElementById('org_desc').style.display = 'none';
    document.getElementById('organiser').style.display = 'block';
    document.getElementById('organiser_link').style.display = 'none';
}

function expand_voter() {
    if (document.getElementById('login_container').style.height == '470px') {
        document.getElementById('organiser_div').classList.remove('col');
        document.getElementById('organiser_div').classList.add('col-3');
        document.getElementById('voter_div').classList.remove('col');
        document.getElementById('voter_div').classList.add('col-9');
        document.getElementById('vtr_icn').style.backgroundColor = '#008B8B';
        document.getElementById('vtr_icn').style.cursor = 'default';
        document.getElementById('voter_link_align').style.cssFloat = 'left';
        document.getElementById('vtr_desc').style.display = 'block';
        document.getElementById('voter').style.display = 'none';
        document.getElementById('voter_link').style.display = 'block';
    }
}

function contract_voter() {
    document.getElementById('voter_div').classList.remove('col-9');
    document.getElementById('voter_div').classList.add('col');
    document.getElementById('organiser_div').classList.remove('col-3');
    document.getElementById('organiser_div').classList.add('col');
    document.getElementById('vtr_icn').style.background = 'none';
    document.getElementById('vtr_icn').style.cursor = 'default';
    document.getElementById('voter_link_align').style.cssFloat = 'none';
    document.getElementById('vtr_desc').style.display = 'none';
    document.getElementById('voter').style.display = 'block';
    document.getElementById('voter_link').style.display = 'none';
}
