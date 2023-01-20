import { EndPoint } from "./endPoint";
export interface TagClass{
    tags: HTMLElement;
    input: HTMLInputElement;
    button: HTMLElement;
    endPoint: EndPoint;
    project: HTMLElement;
    data: object[];
    add(): void;
    delete(): void;
}