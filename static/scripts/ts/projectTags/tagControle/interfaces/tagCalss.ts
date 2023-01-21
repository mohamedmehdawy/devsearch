import { Data } from "./data";
import { EndPoint } from "./endPoint";

export interface TagClass{
    mode: "create" | "update";
    tags: HTMLElement;
    input: HTMLInputElement;
    button: HTMLElement;
    endPoint: EndPoint;
    project: HTMLElement;
    data?: Data;
    headers: {
        "Content-Type": string;
    };

    add(): void;
    delete(): void;
}