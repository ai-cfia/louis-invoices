import json

def safe_format(value):
    if value is None:
        return ''
    s = str(value)
    s = s.replace('\n', ' ')
    s = s.replace(',', ' ')
    s = s.replace('.pickle', '')
    return s

if __name__ == "__main__":
    with open('postprocess.json') as f:
        results = json.load(f)

    fields = ['shipping_address_recipient', 'ship_date', 'shipping_address', 'buxus_count', 'customer_name', 'filename']
    print(','.join(fields))
    for extract in results:
        if extract['buxus_count'] > 0:
            print(','.join([safe_format(extract[field]) for field in fields]))
