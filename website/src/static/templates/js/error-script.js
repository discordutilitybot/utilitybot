function randomColour() {
    let box = document.getElementById('mainBox');
    let colorTemplate = ['#afa09e','#8f847d','#a4a48a','#7d8f78','#83928f','#738da2','#8a8395','#959093'];

    function randomColourPick(colours) {
        return colorTemplate[Math.floor(Math.random()*colorTemplate.length)];
     }

     box.style.backgroundColor = randomColourPick();
}

function textPlace() {
let textToBePlaced = document.getElementById('errorText');
let words = ['The URL may be mispelled or not in the database. Try returning to the homepage.', 
'Sorry! The specified URL is not found on our domain.',
'The specified URL may be incorrect. Click on the button below to return to the UtilityBot homepage.', 
'Oops. Try retyping the URL or returning to the homepage.',
'The URL destination may have been removed or mistyped. Try again, or click the button below.',
"The UtilityBot domain doesn't seem to have that URL. It may be mistyped. Try again, or click the button below.",
'Please retype the URL or return to the UtilityBot homepage.']

function randomitem(words) {
    return words[Math.floor(Math.random()*words.length)];
}

textToBePlaced.innerHTML = randomitem(words);
}
textPlace();
randomColour();
