var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
/**
 * this class controle add and delete tag
 */
export class Tag {
    constructor(tags, input, button, endPoint, project) {
        this.tags = tags;
        this.input = input;
        this.button = button;
        this.endPoint = endPoint;
        this.project = project;
        // init properties
        this.mode = "create";
        this.data = [{ name: "", id: "" }];
        this.headers = {
            "Content-Type": "application/json",
        };
        this.setup();
    }
    /**
     * setup method
     */
    setup() {
        // set mode to update if id is set
        if (this.project.dataset.id) {
            this.mode = "update";
        }
        else {
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
        });
    }
    /**
     * this method add tags to db and return with new data
     * @return all tags
     */
    add() {
        if (this.mode == 'create') {
            let tags = this.input.value.replace(/\s+/g, '').split(',').map((ele) => {
                return { name: ele, id: ele };
            });
            this.data.push(...tags);
            this.render(this.data);
        }
        else {
            this.addCall();
        }
    }
    /**
     * this method send data to server
     */
    addCall() {
        return __awaiter(this, void 0, void 0, function* () {
            const response = yield fetch(`${this.endPoint.base}/${this.endPoint.add}/`, {
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
                });
            }
        });
    }
    /**
     * this method remove tag from db and return tags
     */
    delete() {
        const tags = this.tags.querySelectorAll(".tag");
        tags.forEach(tag => {
            tag.addEventListener("click", () => __awaiter(this, void 0, void 0, function* () {
                const response = yield fetch(`${this.endPoint.base}/${this.endPoint.delete}/`, {
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
                    });
                }
            }));
        });
    }
    /**
     * this function render tags to layout
     * @param data - the all data
     */
    render(data) {
        // reset tags and input value
        this.tags.innerText = "";
        this.input.value = "";
        // add each tag to tags
        for (let tag of data) {
            this.tags.innerHTML += `<section class="tag tag--pill tag--main" data-id='${tag.id}'>${tag.name} ⨯</section>`;
        }
        // call delete to set click events for all tags
        this.delete();
    }
}
