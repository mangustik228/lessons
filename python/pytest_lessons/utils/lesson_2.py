def read_from_file(fp:str) -> list[str]:
    with open(fp, 'r') as file:
        return file.readlines()