import json

if __name__ == "__main__":
    with open('postprocess.json', 'r') as f:
        invoices = json.load(f)
        for index, invoice in enumerate(invoices):
            if invoice['buxus_count'] > 0 and invoice['shipping_address'] is None:
                print(f"{invoice['filename']} missing shipping_address for recipient {invoice['shipping_address_recipient']}")