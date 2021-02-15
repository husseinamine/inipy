# a lightweight ini parser

# how to install 
```sh
pip install ini.py
```

> converts an ini file to a python dictionary

## example ini file
```ini
; main section
[section]
key = value
key2 = "value2"
key3 = 'value3'
```

## reading it using ini.py
```py
import ini

text = open('config.ini', 'r')

config = ini.parse(text)

section = config['section']

print(section['key'], section['key2'], section['key3'])
```

> output 
`value value2 value3`
