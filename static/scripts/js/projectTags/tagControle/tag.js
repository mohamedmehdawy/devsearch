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
        });
    }
    /**
     * this method add tags to db and return with new data
     * @return all tags
     */
    add() {
        return __awaiter(this, void 0, void 0, function* () {
            const response = yield fetch(`${this.endPoint.base}/${this.endPoint.add}/`, {
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
                    for (let tag of data) {
                        this.tags.innerHTML += `<section class="tag tag--pill tag--main">${tag.name} ⨯</section>`;
                    }
                });
            }
        });
    }
    /**
     * this method remove tag to db
     */
    delete() {
    }
}
