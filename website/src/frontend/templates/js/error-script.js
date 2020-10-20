/* JavaScript by PineappleRind (https://github.com/pineapplerind) and Aditya Kapoor (twitter.com/The_Coding_Guru) */

let box = document.getElementById('mainBox'); // The error message
function randomColour() { // sets random color for error message 
    let colorTemplate = ['#afa09e','#8f847d','#a4a48a','#7d8f78','#83928f','#738da2','#8a8395','#959093']; // the colours to pick
    function randomColourPick(colours) {// picks a random color from array
        return colorTemplate[Math.floor(Math.random()*colorTemplate.length)];
     }
     box.style.backgroundColor = randomColourPick(); // sets the colour
}

function textPlace() { 
let textToBePlaced = document.getElementById('errorText');
let words = [ 'Sorry! The specified URL is not found on our domain.',
'The specified URL may be incorrect. Click on the button below to return to the UtilityBot homepage.', 
'Oops. Try retyping the URL or returning to the homepage.',
'The URL destination may have been removed or mistyped. Try again, or click the button below.',
"The UtilityBot domain doesn't seem to have that URL. It may be mistyped. Try again, or click the button below."] // The words to be randomized and placed inside the <p>

function randomitem(words) {
    return words[Math.floor(Math.random()*words.length)];
}

textToBePlaced.innerHTML = randomitem(words); // Sets result of function as <p> text
}
textPlace();
randomColour();
 // invokes function at end

function coords(e) {
let x = e.clientX;
let y = e.clientY;
box.style.color = '#' + x / 5;
}