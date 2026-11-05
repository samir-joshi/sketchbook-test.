import funground as f


def setup():
    f.size(640, 400)


def draw():
    f.background("navy")
    f.fill("tomato")
    f.circle(320, 200, 80)


f.run()
