const fun = async (i) => {
    let s = i
    let n = 1
    while (s * n < 4096) {
        s = Math.floor(s / 2) 
        n = n * 4
    }
    console.log(i,n)
}

const main = async () => {
    for (let i = 0; i < 1100; i++) {
        await fun(i) 
    }
}

main()