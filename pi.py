text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
text1 =  text.replace(".", "").replace(",", "").split()
a = list(map(len, text1))
a = map(str, a)
print("".join(a))
