console.log("Matematyczny Ninja działa!");

const startButton = document.querySelector("button");
const question = document.querySelector("#question");
const math = document.querySelector("#math");
const answer = document.querySelector("#answer");
const checkButton = document.querySelector("#check");
const result = document.querySelector("#result");
const pointsLabel = document.querySelector("#points");

let correctAnswer;
let points = 0;


function newQuestion() {
    let number1 = Math.floor(Math.random() * 10) + 1;
    let number2 = Math.floor(Math.random() * 10) + 1;
    const operation = ["+", "-"][Math.floor(Math.random() * 2)];

    if (operation === "+") {
        correctAnswer = number1 + number2;
    } else {
        if (number1 < number2) {
            [number1, number2] = [number2, number1];
        }

        correctAnswer = number1 - number2;
    }

    math.textContent = `${number1} ${operation} ${number2}`;
}


function checkAnswer() {
    if (answer.value == correctAnswer) {
        result.textContent = "🎉 SUPER!";

        points += 1;
        pointsLabel.textContent = `Punkty: ${points}`;

        newQuestion();
        answer.value = "";
    } else {
        result.textContent = "❌ BŁĄD! Spróbuj jeszcze raz.";
    }
}


startButton.addEventListener("click", function() {
    newQuestion();
    console.log("START!");
    question.textContent = "Ile to jest?";
    answer.focus();
});


checkButton.addEventListener("click", function() {
    checkAnswer();
});


answer.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        checkAnswer();
    }
});