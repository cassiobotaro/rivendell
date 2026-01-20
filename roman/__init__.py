def __getattr__(name):
    name = (
        name.replace("IV", "IIII")
        .replace("IX", "VIIII")
        .replace("XL", "XXXX")
        .replace("XC", "LXXXX")
        .replace("CD", "CCCC")
        .replace("CM", "DCCCC")
    )

    return sum(
        name.count(c) * v for c, v in zip("MDCLXVI", [1000, 500, 100, 50, 10, 5, 1])
    )
