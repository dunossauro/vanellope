# vanellope
File glitcher

| Before | After |
|- | - |
|![alt](./examples/pic.jpg) | ![alt](./examples/new_pic.jpg)|
|command | `vanellope -i examples/pic.jpg -o examples/new_pic.jpg -t 4 -s 30`

## How to install vanellope
```sh
python setup.py install
```

## Usage
```
❯❯❯ vanellope --help
Usage: vanellope [OPTIONS]

  Command line interface to open and write file.

Options:
  -i FILENAME             File to glitch
  -o FILENAME             Result of glitch
  -t INTEGER              Times the operation will be applied
  -size, -bs, -s INTEGER  Size of the part of the file that will be glitched
  --help                  Show this message and exit.
```

## TODO
- [ ] Code more tests
- [ ] Add click option to select glitch operation
- [ ] Add more option to glitch
