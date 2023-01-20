import { Tag } from "./tagControle/tag.js";
// variables
const tags = document.querySelector(".tags");
const input = document.querySelector("#id_tags");
const button = document.querySelector("#add-tag");
const endPoint = {
    base: "http://127.0.0.1:8000/api/projects/tags",
    add: "add",
    delete: "delete"
};
const project = document.querySelector(".project");
// project tags object
const projectTags = new Tag(tags, input, button, endPoint, project);
console.log('hello');
