import { TagClass } from "./interfaces/tagCalss";
import { Data } from "./interfaces/data";
import { EndPoint } from "./interfaces/endPoint";

/**
 * this class controle add and delete tag
 */

export class Tag implements TagClass {
    // init properties
    public mode: "create" | "update" = "create";
    public data: Data = [{name: "", id:""}];
    public headers;
    constructor(public tags: HTMLElement, public input: HTMLInputElement, public button: HTMLElement, public endPoint: EndPoint, public project: HTMLElement) {
        this.headers = {
            "Content-Type": "application/json",
        }
        this.setup();
    }
    /**
     * setup method
     */
    setup() {
        // set mode to update if id is set
        if (this.project.dataset.id) {
            this.mode = "update"
        } else {
            // remove init element
            this.data.pop();
        }
        this.addButton();
        this.delete();
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
    add() {
        if (this.mode == 'create') {
            let tags:Data = this.input.value.replace(/\s+/g, '').split(',').map((ele) => {
                return { name: ele, id: ele }
            });
            
            this.data.push(...tags);
            this.render(this.data)

        }
        else {
            this.addCall();
        }

    }
    /**
     * this method send data to server
     */
    async addCall() {
        const response = await fetch(`${this.endPoint.base}/${this.endPoint.add}/`, {
            method: "POST",
            headers: this.headers,
            body: JSON.stringify({
                projectId: this.project.dataset.id,
                tags: this.input.value,
            })
        });

        if (response.ok) {
            response.json().then(data => {
                this.render(data);
            })
        }
    }
    /**
     * this method remove tag from db and return tags
     */
    delete() {
        const tags = this.tags.querySelectorAll(".tag") as NodeListOf<HTMLElement>
        tags.forEach(tag => {
            tag.addEventListener("click", async () => {
                const response = await fetch(`${this.endPoint.base}/${this.endPoint.delete}/`, {
                    method: "DELETE",
                    headers: this.headers,
                    body: JSON.stringify({
                        projectId: this.project.dataset.id,
                        tagId: tag.dataset.id
                    })
                });
                if (response.ok) {
                    response.json().then(data => {
                        this.render(data);
                    })
                }
            })
        })

    }
    /**
     * this function render tags to layout
     * @param data - the all data
     */
    render(data: { name: string, id: string }[]) {
        // reset tags and input value
        this.tags.innerText = "";
        this.input.value = "";

        // add each tag to tags
        for (let tag of data) {
            this.tags.innerHTML += `<section class="tag tag--pill tag--main" data-id='${tag.id}'>${tag.name} ⨯</section>`
        }
        // call delete to set click events for all tags
        this.delete();
    }
}