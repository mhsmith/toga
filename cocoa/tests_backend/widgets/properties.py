from toga.colors import rgba


def toga_color(color):
    if color:
        return rgba(
            color.redComponent * 255,
            color.greenComponent * 255,
            color.blueComponent * 255,
            color.alphaComponent,
        )
    else:
        return None