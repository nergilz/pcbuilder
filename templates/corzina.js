const first = document.getElementById("first");
const first_min = document.getElementById("first_min");
const first_plus = document.getElementById("first_plus");

first_min.addEventListener("click", () => {
   if (parseInt(first.value) - 1 < 0) return;
   first.value = parseInt(first.value) - 1;
});

first_plus.addEventListener("click", () => {
   first.value = parseInt(first.value) + 1;
});

const two = document.getElementById("two");
const two_min = document.getElementById("two_min");
const two_plus = document.getElementById("two_plus");

two_min.addEventListener("click", () => {
   if (parseInt(two.value) - 1 < 0) return;
   two.value = parseInt(two.value) - 1;
});

two_plus.addEventListener("click", () => {
   two.value = parseInt(two.value) + 1;
});

const three = document.getElementById("three");
const three_min = document.getElementById("three_min");
const three_plus = document.getElementById("three_plus");

three_min.addEventListener("click", () => {
   if (parseInt(three.value) - 1 < 0) return;
   three.value = parseInt(three.value) - 1;
});

three_plus.addEventListener("click", () => {
   three.value = parseInt(three.value) + 1;
});
