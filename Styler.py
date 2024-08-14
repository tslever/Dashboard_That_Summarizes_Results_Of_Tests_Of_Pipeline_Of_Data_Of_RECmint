def create_style(width: int) -> dict:

    style = {}

    if width is not None:
        style["width"] = f"{width}%"

    return style