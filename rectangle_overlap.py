def do_rectangles_overlap(rect1_top_left, rect1_bottom_right, rect2_top_left, rect2_bottom_right):
    x1A, y1A = rect1_top_left
    x2A, y2A = rect1_bottom_right
    x1B, y1B = rect2_top_left
    x2B, y2B = rect2_bottom_right

    if x1A >= x2B or x1B >= x2A:
        return False  # One rectangle is to the left of the other
    if y1A <= y2B or y1B <= y2A:
        return False  # One rectangle is above the other
    return True

# Example usage
if __name__ == "__main__":
    print(do_rectangles_overlap([0, 2], [2, 0], [1, 1], [-1, -1]))
