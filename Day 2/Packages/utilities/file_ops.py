def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

def search_in_file(filename, keyword):
    results = []
    with open(filename, "r") as f:
        for line_num, line in enumerate(f, 1):
            if keyword in line:
                results.append((line_num, line.strip()))
    return results
