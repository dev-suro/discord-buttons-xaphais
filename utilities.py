def get_rgb_from_hex(hex: str):
    """Convert a HEX code to a RGB tuple

    Args:
        hex (str): String in format "FF00FF"

    Returns:
        [tuple]: (r,g,b)
    """
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))