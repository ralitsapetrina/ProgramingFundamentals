def triangle_area(b, h):
    area = b * h / 2
    return f"{area:.12g}"



if __name__ == "__main__":
    base = float(input())
    height = float(input())
    print(triangle_area(base, height))