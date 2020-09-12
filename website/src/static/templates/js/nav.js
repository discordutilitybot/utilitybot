let nav = document.getElementById("navCollapsed");
let openBtn = document.getElementById('openButton')
function openNav() {
    nav.style.opacity = "1";
    openBtn.style.opacity = "0";
  }
  
  function closeNav() {
    nav.style.opacity = "0";
    openBtn.style.opacity = "1";
  }