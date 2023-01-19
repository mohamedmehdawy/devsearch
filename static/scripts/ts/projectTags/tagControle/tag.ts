import {TagClass} from "./interfaces/tagCalss";
import {EndPoint} from "./interfaces/endPoint";
/**
 * this class controle add and delete tag
 */

export class Tag implements TagClass {
    private data;

    constructor(public tags: HTMLCollection, private endPoint: EndPoint) {
        this.tags = tags;
        this.endPoint = endPoint;
        this.data = [{}];
    }
    /**
     * this method add tags to db and return with new data
     * @return all tags
     */
    add() {

    }
    /**
     * this method remove tag to db
     */
    delete() {

    }
}