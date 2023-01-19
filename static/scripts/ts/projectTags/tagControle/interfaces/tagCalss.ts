import { EndPoint } from "./endPoint";
export interface TagClass{
    tags: HTMLCollection;
    endPoint: EndPoint;
    data: object[];
    add(): void;
    delete(): void;
}