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
    projects.innerHTML = "";
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
                    <button class="up" data-value="up" data-project="${data[i].id}">&#43;</button>
                    <button class="down" data-value="down" data-project="${data[i].id}">&#8722;</button>

                </section>
            </section>
        `;
    }
    voteEvents();
}

// voteEvents
function voteEvents() {
    const end_point = "http://127.0.0.1:8000/api/projects/vote/";
    const buttons = document.querySelectorAll(".project .vote button");
    
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const project = button.dataset.project;
            const value = button.dataset.value;
            
            fetch(`${end_point}${project}/`, {
                method: "post",
                headers: {
                    'Content-Type': 'application/json',
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxMDY2NDQ2LCJpYXQiOjE2NzA5ODAwNDYsImp0aSI6IjVjODA2ZGQ1ZmFiMDQ1YmY4OGMwNDgzNzA0NDBiMmM3IiwidXNlcl9pZCI6MX0.uHqIth72_emyK1JfJq7L7gudeZKfHFhUvOQPy05xajQ",
                },
                body: JSON.stringify({
                    value,
                    body: "test body"
                })
            }).then(response => response.json()).then(data => {
                console.log(data)
                getProjects();
            })
        })
    })
}

getProjects();
