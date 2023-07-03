import json

def suppress_none(value):
    if value is None:
        return ''
    s = str(value)
    s = s.replace('\n', ' ')
    s = s.replace(',', ' ')
    s = s.replace('.pickle', '')
    return s

if __name__ == "__main__":
    with open('fillin.json') as f:
        results = json.load(f)

    fields = ['customer_name', 'customer_address', 'shipping_address', 'shipping_address_recipient', 'date', 'filename', 'buxus_count']
    print(','.join(fields))
    for extract in results:
        print(','.join([suppress_none(extract[field]) for field in fields]))
