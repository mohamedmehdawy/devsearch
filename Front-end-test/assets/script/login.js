const form = document.querySelector("form");
const end_point = `http://127.0.0.1:8000/api/token/`;

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    // set form data
    const formData = {
        username: form.username.value,
        password: form.password.value,
    };

    // call api
    const response = await fetch(end_point, {
        method: "post",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    });
    if(response.ok) {
        response.json().then(data => {
            localStorage.setItem("token", data.access);
            // redirect to home page
            window.location = '/';
        })
    }
})