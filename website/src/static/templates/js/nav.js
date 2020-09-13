let nav = document.getElementById("navCollapsed");
let openBtn = document.getElementById('openButton')

function navView() {
  if (nav.style.opacity = "0") {
    nav.style.opacity = "1";
    openBtn.setAttribute("onclick", "navClose();");
    document.addEventListener("click", function() {
      navClose();
    });
  }
}

function navClose() {
  if (nav.style.opacity = "1") {
    document.addEventListener("click", function() {
      nav.style.opacity = "0";
      openBtn.setAttribute("onclick", "navView();");
    });
    
  }
}