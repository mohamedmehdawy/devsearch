let searchForm = document.querySelector("#search-form") as HTMLFormElement;
let links = document.querySelectorAll(
    ".pagination li a"
) as NodeListOf<HTMLAnchorElement>;

links.forEach((link): void => {
    link.addEventListener("click", (e: Event): void => {
        e.preventDefault();
        let searchValue = searchForm.querySelector("input")!.value;
        let target = `?search_query=${searchValue}&page=${link.dataset.page}`;
        window.location.href = target;
    });
});
