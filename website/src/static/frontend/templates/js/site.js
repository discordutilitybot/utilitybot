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

function showModCommands() {
  let tableMod = document.getElementById('tableM');
  let trigMod = document.getElementById('trigM');
  let iconMod = document.getElementById('iconM');
  if (tableMod.style.display = 'none') {
      tableMod.style.display = 'block'; // make it null
      iconMod.classList.remove('fa-angle-down');
      iconMod.classList.add("fa-angle-up");
      trigMod.setAttribute("onclick","hideModCommands()");
  } 
}

function showFunCommands() {
  let tableFun = document.getElementById('tableF');
  let trigFun = document.getElementById('trigF');
  let iconFun = document.getElementById('iconF');

  if (tableFun.style.display = 'none') {
    tableFun.style.display = 'block'; // make it null
    iconFun.classList.remove('fa-angle-down');
    iconFun.classList.add("fa-angle-up");
    trigFun.setAttribute("onclick","hideFunCommands()");
  } 
}

function hideModCommands() {
  let tableMod = document.getElementById('tableM');
  let trigMod = document.getElementById('trigM');
  let iconMod = document.getElementById('iconM');
  if (tableMod.style.display = 'block') {
      tableMod.style.display = 'none'; // make it null
      iconMod.classList.remove('fa-angle-up');
      iconMod.classList.add("fa-angle-down");
      trigMod.setAttribute("onclick","showModCommands()");
  } 
}

function  hideFunCommands() {
  let tableFun = document.getElementById('tableF');
  let trigFun = document.getElementById('trigF');
  let iconFun = document.getElementById('iconF');

  if (tableFun.style.display = 'block') {
    tableFun.style.display = 'none'; // make it null
    iconFun.classList.remove('fa-angle-up');
    iconFun.classList.add("fa-angle-down");
    trigFun.setAttribute("onclick","showFunCommands()");
  } 
}