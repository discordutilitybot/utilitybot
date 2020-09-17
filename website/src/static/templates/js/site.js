let nav = document.getElementById("navCollapsed"); // The navbar
let openBtn = document.getElementById('openButton'); // The trigger

function navView() { // Open nav function
  if (nav.style.height = "0%") { // If it is invisible,
    nav.style.height = "100%"; // Make it visible
    openBtn.setAttribute("onclick", "navClose();"); // Sets button to close navbar function
  }
}

function navClose() { // Close navbar function
  if (nav.style.height = "100%") { // If it's visible,
    nav.style.height = "0%"; // Make it invisible
    openBtn.setAttribute("onclick", "navView();") // Sets button to open nav function
  }
}
