import { TagClass } from "./interfaces/tagCalss";
import { EndPoint } from "./interfaces/endPoint";
/**
 * this class controle add and delete tag
 */

export class Tag implements TagClass {
    public data;

    constructor(public tags: HTMLElement, public input: HTMLInputElement, public button: HTMLElement, public endPoint: EndPoint, public project: HTMLElement) {
        this.data = [{}];
        this.setup();
    }
    /**
     * setup method
     */
    setup() {
        this.addButton();
    }
    /**
     * call add function when click in button
     */
    addButton() {
        this.button.addEventListener("click", () => {
            this.add();
        })
    }
    /**
     * this method add tags to db and return with new data
     * @return all tags
     */
    async add() {
        const response = await fetch(`${this.endPoint.base}/${this.endPoint.add}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0MjQ5MTQ5LCJpYXQiOjE2NzQxNjI3NDksImp0aSI6ImVlZTNmNGY4YjJhMzQwODJiNTRhMmYxOTliMmVhY2FlIiwidXNlcl9pZCI6MX0.JuKZakLsfi7lRBuPgj1auGhXSgjvUow1Wu3Jzn5ArUg"
            },
            body: JSON.stringify({
                projectId: this.project.dataset.id,
                tags: this.input.value,
            })
        });
        
        if (response.ok) {
            response.json().then(data => {
                // reset tags and input value
                this.tags.innerText = "";
                this.input.value = "";

                // add each tag to tags
                for(let tag of data) {
                    this.tags.innerHTML += `<section class="tag tag--pill tag--main">${tag.name} ⨯</section>`
                }
            })
        }
    }
    /**
     * this method remove tag to db
     */
    delete() {
        
    }
}