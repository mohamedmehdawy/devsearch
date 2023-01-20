"use strict";
let searchForm = document.querySelector("#search-form");
let links = document.querySelectorAll(".pagination li a");
links.forEach((link) => {
    link.addEventListener("click", (e) => {
        e.preventDefault();
        let searchValue = searchForm.querySelector("input").value;
        let target = `?search_query=${searchValue}&page=${link.dataset.page}`;
        window.location.href = target;
    });
});
