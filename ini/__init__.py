def parse(text):
    data = {}
    section = ''

    for line in text.split('\n'):
        if line.startswith(';'):
            continue

        elif line.startswith('[') and line.endswith(']'):
            line = line.replace('[', '')
            line = line.replace(']', '')
            
            section = line.strip()
            
            if not data.get(section):
                data[section] = {}

        else:
            if "=" in line:
                key, value = line.split('=')
            
                key = key.replace("\"", "")
                key = key.replace("\'", "")
                key = key.strip()
                
                value = value.replace("\"", "")
                value = value.replace("\'", "")
                value = value.strip()

                data[section][key] = value

    return data

def convert(data):
    text = ""
    for section in data:
        text += "[%s]\n" % section

        for key in data[section]:
            text += "%s = %s\n" % (key, data[section][key])

        text += "\n"

    return text.strip()