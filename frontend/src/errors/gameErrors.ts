export class BetPredictionError extends Error {
    constructor(message: string) {
        super(message);
        this.name = "BetPredictionError";
    }
}