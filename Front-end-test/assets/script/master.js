const token = localStorage.getItem("token");

// redirect
/**
 * this function redirect to passed url
 * @param target - the url target
 */
function redirect(target) {
    window.location = `/${target}.html`;
}
// handel login
function handelLogin() {
    const login = document.getElementById("login");
    const logout = document.getElementById("logout");

    // check if token found
    if(token) {
        login.remove();
    } else {
        logout.remove();
    }

    // logout click
    logout.addEventListener("click", (e)=> {
        e.preventDefault();
        localStorage.removeItem("token");
        redirect("pages/login")
    })
}
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
                    <button class="up" data-value="up" data-project="${
                        data[i].id
                    }">&#43;</button>
                    <button class="down" data-value="down" data-project="${
                        data[i].id
                    }">&#8722;</button>

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

    buttons.forEach((button) => {
        button.addEventListener("click", async () => {
            const project = button.dataset.project;
            const value = button.dataset.value;
            if (token) {
                const respsone = await fetch(`${end_point}${project}/`, {
                    method: "post",
                    headers: {
                        "Content-Type": "application/json",
                        Authorization: `Bearer ${token}`,
                    },
                    body: JSON.stringify({
                        value,
                        body: "test body",
                    }),
                });
                if (respsone.ok) {
                    respsone.json().then((data) => {
                        console.log(data);
                        getProjects();
                    });
                } else {
                    redirect("pages/login")
                }
            } else {
                redirect("pages/login")
            }
        });
    });
}
handelLogin();
getProjects();
