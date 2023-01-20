import { Tag } from "./tagControle/tag.js";

// variables
const tags = document.querySelector(".tags") as HTMLElement;
const input = document.querySelector("#id_tags") as HTMLInputElement;
const button = document.querySelector("#add-tag") as HTMLElement;
const endPoint = {
    base: "http://127.0.0.1:8000/api/projects/tags",
    add: "add",
    delete: "delete"
};
const project = document.querySelector(".project") as HTMLElement;

// project tags object
const projectTags = new Tag(tags, input, button,endPoint, project);
console.log('hello')