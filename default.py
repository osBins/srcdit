data = "key1=value1\n\
key2=value2\n\
key3=value3"

def write_default(file, data):
    with open(file, "w") as f:
        f.write(data)


write_default('test', data)