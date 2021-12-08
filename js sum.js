const sum = (...args) => {
    let total = 0;
    for (const x of args) {
        total += x;
    }
    return total;
};


const result = sum(23, 451, 78, 13, 896, 102, 2, 741, 236, 562, 85, 4, 96);
console.log(result);
