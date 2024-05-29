document.addEventListener("DOMContentLoaded", function () {
    let button = document.querySelector(".button");
    let recto = document.querySelector(".recto");

    button.addEventListener("click", function () {
        if (getComputedStyle(recto).display != "none") {
            recto.style.display = "none";
        } else {
            recto.style.display = "block";
        }
    });
});
