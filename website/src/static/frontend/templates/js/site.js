let nav = document.getElementById("navCollapsed"); // The navbar
let openBtn = document.getElementById('openButton'); // The trigger
let navContents = document.getElementById('navList'); // The navbar contents

function navView() { // Open nav function
  if (nav.style.height = "0%") { // If it is invisible,
    nav.style.height = "100%"; // Make it visible
    openBtn.setAttribute("onclick", "navClose();"); // Sets button to close navbar function
    navContents.style.display = 'block'; // Nav contents made visible on opening nav
  }
}

function navClose() { // Close navbar function
  if (nav.style.height = "100%") { // If it's visible,
    nav.style.height = "0%"; // Make it invisible
    openBtn.setAttribute("onclick", "navView();") // Sets button to open nav function
    setTimeout(function(){navContents.style.display = 'none';}, 700) // Nav contents made invisible after 0.7s of closing nav
  }
}

/*The following code was a last resort so it's not the best :(*/

function showModCommands() {
  let tableMod = document.getElementById('tableM'); // the table
  let trigMod = document.getElementById('trigM'); // the trigger 
  let iconMod = document.getElementById('iconM'); // the down arrow
  if (tableMod.style.display = 'none') { // if it is not shown:
      tableMod.style.display = 'block'; // show it,
      tableMod.style.animationName = 'float-down';
      iconMod.classList.remove('fa-angle-down'); // change arrow,
      iconMod.classList.add("fa-angle-up");
      trigMod.setAttribute("onclick","hideModCommands()"); // and set onclick function to hide the commands
  } 
}

function showFunCommands() {
  let tableFun = document.getElementById('tableF'); // this is basically the same as above.
  let trigFun = document.getElementById('trigF');
  let iconFun = document.getElementById('iconF');

  if (tableFun.style.display = 'none') {
    tableFun.style.display = 'block';
    tableFun.style.animationName = 'float-down';
    iconFun.classList.remove('fa-angle-down');
    iconFun.classList.add("fa-angle-up");
    trigFun.setAttribute("onclick","hideFunCommands()");
  } 
}

function showInfoCommands() {
  let tableInf = document.getElementById('tableI'); // this is basically the same as above.
  let trigInf = document.getElementById('trigI');
  let iconInf = document.getElementById('iconI');

  if (tableInf.style.display = 'none') {
    tableInf.style.display = 'block';
    tableInf.style.animationName = 'float-down';
    tableInf.style.animationDirection = 'n';
    iconInf.classList.remove('fa-angle-down');
    iconInf.classList.add("fa-angle-up");
    trigInf.setAttribute("onclick","hideInfoCommands()");
  } 
}

function showUtilCommands() {
  let tableUtil = document.getElementById('tableU'); // this is basically the same as above.
  let trigUtil = document.getElementById('trigU');
  let iconUtil = document.getElementById('iconU');

  if (tableUtil.style.display = 'none') {
    tableUtil.style.display = 'block';
    tableUtil.style.animationName = 'float-down';
    iconUtil.classList.remove('fa-angle-down');
    iconUtil.classList.add("fa-angle-up");
    trigUtil.setAttribute("onclick","hideUtilCommands()");
  } 
}

function hideModCommands() {
  let tableMod = document.getElementById('tableM');
  let trigMod = document.getElementById('trigM');
  let iconMod = document.getElementById('iconM');
  if (tableMod.style.display = 'block') {
      setTimeout(function(){tableMod.style.display = 'none'}, 400);
      iconMod.classList.remove('fa-angle-up');
      tableMod.style.animationName = 'float-up';
      iconMod.classList.add("fa-angle-down");
      trigMod.setAttribute("onclick","showModCommands()");
  } 
}

function hideFunCommands() {
  let tableFun = document.getElementById('tableF');
  let trigFun = document.getElementById('trigF');
  let iconFun = document.getElementById('iconF');

  if (tableFun.style.display = 'block') {
    setTimeout(function(){tableFun.style.display = 'none'}, 400);
    tableFun.style.animationName = 'float-up';
    iconFun.classList.remove('fa-angle-up');
    iconFun.classList.add("fa-angle-down");
    trigFun.setAttribute("onclick","showFunCommands()");
  } 
}

function hideInfoCommands() {
  let tableInf = document.getElementById('tableI');
  let trigInf = document.getElementById('trigI');
  let iconInf = document.getElementById('iconI');

  if (tableInf.style.display = 'block') {
    setTimeout(function(){tableInf.style.display = 'none'}, 400);
    tableInf.style.animationName = 'float-up';
    iconInf.classList.remove('fa-angle-up');
    iconInf.classList.add("fa-angle-down");
    trigInf.setAttribute("onclick","showInfoCommands()");
  } 
}

function hideUtilCommands() {
  let tableUtil = document.getElementById('tableU');
  let trigUtil = document.getElementById('trigU');
  let iconUtil = document.getElementById('iconU');

  if (tableUtil.style.display = 'block') {
    setTimeout(function(){tableUtil.style.display = 'none'}, 400);
    tableUtil.style.animationName = 'float-up';
    iconUtil.classList.remove('fa-angle-up');
    iconUtil.classList.add("fa-angle-down");
    trigUtil.setAttribute("onclick","showUtilCommands()");
  } 
}

/* The following code is based off of: https://bit.ly/32C1vfo
Comments added by me. */

let acc = document.getElementsByClassName("faq-question"); // accordion variable

for (let i = 0; i < acc.length; i++) {
    acc[i].onclick = function() { // When click is detected execute the following
        let content = this.nextElementSibling; // The accordion content
        if (content.style.maxHeight) { // if the height is not null...
            content.style.maxHeight = null; // make it null
        } else {
            content.style.maxHeight = content.scrollHeight + "px"; // If it's null, make it not null
        }
    }
}