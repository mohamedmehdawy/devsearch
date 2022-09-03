"use strict";

// Invoke Functions Call on Document Loaded
// document.addEventListener("DOMContentLoaded", function () {
//   hljs.highlightAll();
// });
// alert
var alerts = document.querySelectorAll(".alert");
alerts.forEach(function (ele) {
  ele.querySelector(".alert__close").addEventListener("click", function () {
    ele.style.display = "none";
  });
});