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

text = open('config.ini', 'r').read()

config = ini.parse(text)

section = config['section']

print(section['key'], section['key2'], section['key3'])
```
> output 
```
value value2 value3
```

----------------------------------------

# converting python dict to ini
```py
import ini

config = ini.convert({"section": {"key": "value"}, "section2": {"key2": "value2"}})


print(config)
```
> output
```ini
[section]
key = value

[section2]
key2 = value2
```