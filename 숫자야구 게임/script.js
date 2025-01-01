// Make Attempts Variables
const maxAttempts = 9;
let attempts = maxAttempts;
// Make a random Answer Array
const getRandomInt = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
};
const AnswerArray = [
    getRandomInt(1,9),
    getRandomInt(1,9),
    getRandomInt(1,9),
]
// operation with click a 확인하기 button
function check_numbers(){
    const inputHTMLcollection = document.querySelectorAll('.input-field');
    const inputArray = Array.from(inputHTMLcollection);



    attempts--;
    console.log(AnswerArray);
    console.log(attempts);
}