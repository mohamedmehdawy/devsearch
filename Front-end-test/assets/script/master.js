// get projects
async function getProjects() {
    const end_point = "http://127.0.0.1:8000/api/projects/";
    await fetch(end_point)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            buildProjects(data);
        });
}

// build projects
function buildProjects(data) {
    let projects = document.querySelector("#projects");

    for (let i = 0; i < data.length; i++) {
        projects.innerHTML += `
            <section class="project">
                <section class="image">
                    <img src="http://127.0.0.1:8000${data[i].image}" />
                </section>
                <section class="info">
                    <h3>${data[i].title}</h3>
                    <p>${data[i].description.substring(0, 150)}...</p>
                </section>
                <section class="vote">
                    <button class="up">&#43;</button>
                    <button class="down">&#8722;</button>

                </section>
            </section>
        `;
    }
}
getProjects();
