let nav = document.getElementById("navCollapsed"); // The navbar
let openBtn = document.getElementById('openButton'); // The trigger
let navContents = document.getElementById('navList'); // The navbar contents

let main = document.getElementById('main');
let footer = document.getElementById('foot')
function navView() { // Open nav function
  if (nav.style.width = "0px") { // If it is invisible,
    nav.style.width = "350px"; // Make it visible
    openBtn.setAttribute("onclick", "navClose();"); // Sets button to close navbar function
    setTimeout(function(){navContents.style.animationName = 'float-right'; navContents.style.display = 'block';}, 700); // Loading animation for nav contents
    main.style.marginLeft = '350px';
    footer.style.marginLeft = '350px';
  }
}

function navClose() { // Close navbar function
  if (nav.style.width = "350px") { // If it's visible,
    nav.style.width = "0px"; // Make it invisible
    openBtn.setAttribute("onclick", "navView();") // Sets button to open nav function
    setTimeout(function(){navContents.style.display = 'none';}, 700); // Nav contents made invisible after 0.7s of closing nav
    main.style.marginLeft = '0';
    footer.style.marginLeft = '0';
  }
}

/* This next bit of code is a last resort so it's HORRIBLE. T-T */

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
    if (this.style.maxHeight != '600px') {
          this.style.maxHeight = '600px'; // make it null
    } else {
      this.style.maxHeight = '29px';
    }
  }
}
