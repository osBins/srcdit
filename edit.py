import subprocess

def get_keys():
    pass

def get_values():
    pass

def key_value_edit(file, key, value):
    with open(file, "r") as f:
        data = f.read()
        lines = data.split("\n")
        
        for i in range(len(lines)):
            if lines[i].find(key) != -1:
                lines[i] = f"{key}={value}"
                break
        else:
            print("Key not found")
            return
    
    with open(file, "w") as f:
        data = '\n'.join(lines)
        f.write(data)
        print("Written out")

key_value_edit('test', "key3", "value1")
