let nav = document.getElementById("navCollapsed"); // The navbar
let openBtn = document.getElementById('openButton'); // The trigger
let navContents = document.getElementById('navList'); // The navbar contents

function navView() { // Open nav function
  if (nav.style.height = "0%") { // If it is invisible,
    nav.style.height = "100%"; // Make it visible
    openBtn.setAttribute("onclick", "navClose();"); // Sets button to close navbar function
    navContents.style.animationName = 'float-right';
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

/* This next bit of code is a last resort so it's HORRIBLE. T-T */
function infoCommands() {
  if (document.getElementById('infoCommands').style.maxHeight = '29px') {
    document.getElementById('infoCommands').style.maxHeight = '600px';
    document.getElementById('infoCommands').setAttribute("onclick", "hideInfoCommands()");
  } 
}
function hideInfoCommands() {
  document.getElementById('infoCommands').style.maxHeight = '29px';
  document.getElementById('infoCommands').setAttribute("onclick", "infoCommands()");
}

function utilCommands() {
  if (document.getElementById('utilCommands').style.maxHeight = '29px') {
    document.getElementById('utilCommands').style.maxHeight = '150px';
    document.getElementById('utilCommands').setAttribute("onclick", "hideUtilCommands()");
  } 
}
function hideUtilCommands() {
  document.getElementById('utilCommands').style.maxHeight = '29px';
  document.getElementById('utilCommands').setAttribute("onclick", "utilCommands()");
}

function modCommands() {
  if (document.getElementById('modCommands').style.maxHeight = '29px') {
    document.getElementById('modCommands').style.maxHeight = '600px';
    document.getElementById('modCommands').setAttribute("onclick", "hideModCommands()");
  } 
}
function hideModCommands() {
  document.getElementById('modCommands').style.maxHeight = '29px';
  document.getElementById('modCommands').setAttribute("onclick", "modCommands()");
}

function funCommands() {
  if (document.getElementById('funCommands').style.maxHeight = '29px') {
    document.getElementById('funCommands').style.maxHeight = '600px';
    document.getElementById('funCommands').setAttribute("onclick", "hideFunCommands()");
  } 
}
function hideFunCommands() {
  document.getElementById('funCommands').style.maxHeight = '29px';
  document.getElementById('funCommands').setAttribute("onclick", "funCommands()");
}

function openInNewTab(url) {
  var win = window.open(url, '_blank');
  win.focus();
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
