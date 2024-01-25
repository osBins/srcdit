# srcdit

Edit and source dotfiles directly from the terminal

### Usage
```bash
srcdit <file> <key=value>
```

Example -
```bash
srcdit .zshrc ZSH_THEME="powerlevel10k/powerlevel10k"
```

### Work In Progress!
* Source edited files (through shell script, since a subprocess spawns through Python) - Wrap Python script in a Shell script, but that won't allow sourcing for the PyPi version. Might need to port.
* Debug

### Source Code
[GitHub Link](https://github.com/osBins/srcdit)
