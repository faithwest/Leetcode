function solution(P, Q) {
    let n = P.length;
    let m = Q.length;

    if (n === m) {
        let pString = P.toString();
        let qString = Q.toString();
        let combine = pString + qString;
        console.log(combine);

        let letterCounts = {};

        for (let i = 0; i < combine.length; i++) {
            let currentLetter = combine[i];
            console.log(` current ${currentLetter}`);
            letterCounts[currentLetter] = (letterCounts[currentLetter] || 0) + 1;
            console.log(`the letters ${letterCounts[currentLetter]}`);
        }

        let repeatedLetters = [];

        for (let letter in letterCounts) {
            if (letterCounts.hasOwnProperty(letter) && letterCounts[letter] > 1) {
                repeatedLetters.push(letter + ' #' + letterCounts[letter]);
            }
        }

        return repeatedLetters;
    }
}

// Example usage with threshold set to 1
let result = solution(["bacad"], ["abada"]);
console.log(result);
