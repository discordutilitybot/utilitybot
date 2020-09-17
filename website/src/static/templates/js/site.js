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

// The following code is based off of: https://bit.ly/32C1vfo

let acc = document.getElementsByClassName("faq-question");

for (let i = 0; i < acc.length; i++) {
    acc[i].onclick = function() {
        let content = this.nextElementSibling;
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    }
}