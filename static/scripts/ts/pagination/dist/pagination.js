var searchForm = document.querySelector("#search-form");
var links = document.querySelectorAll(".pagination li a");
links.forEach(function (link) {
    link.addEventListener("click", function (e) {
        e.preventDefault();
        var searchValue = searchForm.querySelector("input").value;
        var target = "?search_query=" + searchValue + "&page=" + link.dataset.page;
        window.location.href = target;
    });
});
