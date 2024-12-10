document.querySelector("form").addEventListener("submit", function(e) {
    let answer = document.querySelector("textarea").value;
    if (answer.trim() === "") {
        alert("Please write your answer before submitting!");
        e.preventDefault();
    }
});
