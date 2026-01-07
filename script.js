const form = document.querySelector("form");
const loader = document.querySelector(".loader");
const textarea = document.querySelector("textarea");

form.addEventListener("submit", () => {
    loader.style.display = "block";
});

textarea.focus();
