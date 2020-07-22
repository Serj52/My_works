# You are given a sequence of strings. You should join these strings into a chunk of text where the initial strings are separated by commas.
# As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left",
# even if it's a part of another word. All strings are given in lowercase.


def left_join(text):
    if ',' not in text:
        return (','.join(text)).replace('right','left')
    else:
        return ' '.join(text)

assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"