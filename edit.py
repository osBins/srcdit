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
            print("Key not found.")
            while True:
                yes_no = input("Add new? (y/n)\n")
                if yes_no.lower() in ["yes", "y"]:
                    lines.append(f"{key}={value}")
                    break
                elif yes_no.lower() in ["no", "n"]:
                    print("Not written.")
                    return
                else:
                    print("Invalid input. Please enter yes/no.")
    
    with open(file, "w") as f:
        data = '\n'.join(lines)
        f.write(data)
        print("Written out")

def main():
    key_value_edit('test', "key4", "value1")

if __name__ == "__main__":
    main()
