// Invoke Functions Call on Document Loaded
// document.addEventListener("DOMContentLoaded", function () {
//   hljs.highlightAll();
// });

// alert
const alerts = document.querySelectorAll(".alert");

alerts.forEach((ele) => {
  ele.querySelector(".alert__close").addEventListener("click", () => {
    ele.style.display = "none";
  });
});
