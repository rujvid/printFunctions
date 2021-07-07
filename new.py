def swapLetterCase(letter):
    return letter.swapCase()


inp = input()
print("".join(c.swapcase() for c in inp))

inputLetters = [c for c in inp]
print(*inputLetters)
print("".join(map(lambda c: c.swapcase(), inputLetters)))