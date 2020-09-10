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
