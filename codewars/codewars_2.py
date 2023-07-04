

def make_readable(v: int):
    return f"{v//3600:02}:{v//60%60:02}:{v%60:02}"


print(f"{'hello'[::2]}")


print(f"{'hello'[::]}")


print(f"{'hello'[::-1]}")
