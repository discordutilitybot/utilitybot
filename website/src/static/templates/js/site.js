let nav = document.getElementById("navCollapsed");
let openBtn = document.getElementById('openButton')

function navView() {
  if (nav.style.height = "0%") {
    nav.style.height = "100%";
    openBtn.setAttribute("onclick", "navClose();");
  }
}

function navClose() {
  if (nav.style.height = "100%") {
    nav.style.height = "0%";
    openBtn.setAttribute("onclick", "navView();")
  }
}