def html_string_to_file(obj, filepath):
    with open(filepath, 'w') as file:
        file.write(obj)
        