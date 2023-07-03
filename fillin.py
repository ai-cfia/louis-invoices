import json
import regex

if __name__ == "__main__":
    with open('postprocess.json', 'r') as f:
        invoices = json.load(f)
        invoices.sort(key=lambda x: x['filename'])
    lookup_address = {}
    for index, invoice in enumerate(invoices):
        if invoice['shipping_address'] is not None and len(invoice['shipping_address']) > 0 and invoice['shipping_address_recipient'] is not None: 
            lookup_address[invoice['shipping_address_recipient']] = invoice['shipping_address']
    print(json.dumps(lookup_address, indent=4))
    for index, invoice in enumerate(invoices):
        if invoice['shipping_address'] is None:
            if invoice['shipping_address_recipient'] is not None:
                prev_invoice = invoices[index-1]
                if prev_invoice['shipping_address_recipient'] == invoice['shipping_address_recipient']:
                    invoice['shipping_address'] = prev_invoice['shipping_address']
                    prev_invoice['buxus_items'].extend(invoice['buxus_items'])
                    total = sum([i['item_quantity'] for i in invoice['buxus_items']])
                    prev_invoice['buxus_count'] += total
                    del invoices[index]
    for index, invoice in enumerate(invoices):
        if invoice['shipping_address'] is None: 
            candidate_address = lookup_address.get(invoice['shipping_address_recipient'])
            if candidate_address:
                invoice['shipping_address'] = candidate_address
            else:
                r = '(' + regex.escape(invoice['shipping_address_recipient']) + '){e<=2}'
                for (key, value) in lookup_address.items():
                    if regex.match(r, key):
                        invoice['shipping_address'] = value
                        break
    
    with open('fillin.json', 'w+') as f:
        filtered = []
        filtered.extend(filter(lambda i: i['buxus_count'] > 0, invoices))
        json.dump(filtered, f)