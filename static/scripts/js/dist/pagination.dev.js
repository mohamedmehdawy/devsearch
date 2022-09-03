"use strict";

var searchForm = document.querySelector("#search-form");
var links = document.querySelectorAll(".pagination li a");
links.forEach(function (link) {
  link.addEventListener("click", function (e) {
    e.preventDefault();
    var searchValue = searchForm.querySelector("input").value;
    var target = "?search_query=".concat(searchValue, "&page=").concat(link.dataset.page);
    window.location.href = target;
  });
});