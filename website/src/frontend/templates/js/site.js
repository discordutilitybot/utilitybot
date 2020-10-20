/* JavaScript by PineappleRind (https://github.com/pineapplerind) and Aditya Kapoor (twitter.com/The_Coding_Guru) */

let nav = document.getElementById("navCollapsed"); // The navbar
let openBtn = document.getElementById('openButton'); // The trigger
let navContents = document.getElementById('navList'); // The navbar contents

let main = document.getElementById('main');
function navView() { // Open nav function
  if (nav.style.width = "0px") { // If it is invisible,
    nav.style.width = "350px"; // Make it visible
    navContents.style.display = 'block';
    openBtn.setAttribute("onclick", "navClose();"); // Sets button to close navbar function
    navContents.style.animationName = 'float-appear'; 
    main.style.marginLeft = '350px';
  }
}

function navClose() { // Close navbar function
  if (nav.style.width = "350px") { // If it's visible,
  nav.style.width = "0px"; // Make it invisible
  main.style.marginLeft = '0';

    setTimeout(function(){ // Timeout for display:none; so that it doesn't unexpectedly disappear
      navContents.style.display = 'none';
    },900)
    openBtn.setAttribute("onclick", "navView();") // Sets button to open nav function
  }
}

function openInNewTab(url) {
  var win = window.open(url, '_blank');
  win.focus();
}

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

let commandsTitle = document.getElementsByClassName("commands-title"); // accordion variable
for (let i = 0; i < commandsTitle.length; i++) {
  commandsTitle[i].onclick = function() { // When click is detected execute the following // The accordion content
    if (this.style.maxHeight != '475px') {
          this.style.maxHeight = '475px'; // make it null
    } else {
      this.style.maxHeight = '40px';
    }
  }
}