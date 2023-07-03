import pickle
import regex
import os
import json

def print_invoice(idx, invoice):
    
    print("--------Recognizing invoice #{}--------".format(idx + 1))
    vendor_name = invoice.fields.get("VendorName")
    if vendor_name:
        print(
            "Vendor Name: {} has confidence: {}".format(
                vendor_name.value, vendor_name.confidence
            )
        )
    vendor_address = invoice.fields.get("VendorAddress")
    if vendor_address:
        print(
            "Vendor Address: {} has confidence: {}".format(
                vendor_address.value, vendor_address.confidence
            )
        )
    vendor_address_recipient = invoice.fields.get("VendorAddressRecipient")
    if vendor_address_recipient:
        print(
            "Vendor Address Recipient: {} has confidence: {}".format(
                vendor_address_recipient.value, vendor_address_recipient.confidence
            )
        )
    customer_name = invoice.fields.get("CustomerName")
    if customer_name:
        print(
            "Customer Name: {} has confidence: {}".format(
                customer_name.value, customer_name.confidence
            )
        )
    customer_id = invoice.fields.get("CustomerId")
    if customer_id:
        print(
            "Customer Id: {} has confidence: {}".format(
                customer_id.value, customer_id.confidence
            )
        )
    customer_address = invoice.fields.get("CustomerAddress")
    if customer_address:
        print(
            "Customer Address: {} has confidence: {}".format(
                customer_address.value, customer_address.confidence
            )
        )
    customer_address_recipient = invoice.fields.get("CustomerAddressRecipient")
    if customer_address_recipient:
        print(
            "Customer Address Recipient: {} has confidence: {}".format(
                customer_address_recipient.value,
                customer_address_recipient.confidence,
            )
        )
    invoice_id = invoice.fields.get("InvoiceId")
    if invoice_id:
        print(
            "Invoice Id: {} has confidence: {}".format(
                invoice_id.value, invoice_id.confidence
            )
        )
    invoice_date = invoice.fields.get("InvoiceDate")
    if invoice_date:
        print(
            "Invoice Date: {} has confidence: {}".format(
                invoice_date.value, invoice_date.confidence
            )
        )
    invoice_total = invoice.fields.get("InvoiceTotal")
    if invoice_total:
        print(
            "Invoice Total: {} has confidence: {}".format(
                invoice_total.value, invoice_total.confidence
            )
        )
    due_date = invoice.fields.get("DueDate")
    if due_date:
        print(
            "Due Date: {} has confidence: {}".format(
                due_date.value, due_date.confidence
            )
        )
    purchase_order = invoice.fields.get("PurchaseOrder")
    if purchase_order:
        print(
            "Purchase Order: {} has confidence: {}".format(
                purchase_order.value, purchase_order.confidence
            )
        )
    billing_address = invoice.fields.get("BillingAddress")
    if billing_address:
        print(
            "Billing Address: {} has confidence: {}".format(
                billing_address.value, billing_address.confidence
            )
        )
    billing_address_recipient = invoice.fields.get("BillingAddressRecipient")
    if billing_address_recipient:
        print(
            "Billing Address Recipient: {} has confidence: {}".format(
                billing_address_recipient.value,
                billing_address_recipient.confidence,
            )
        )
    shipping_address = invoice.fields.get("ShippingAddress")
    if shipping_address:
        print(
            "Shipping Address: {} has confidence: {}".format(
                shipping_address.value, shipping_address.confidence
            )
        )
    shipping_address_recipient = invoice.fields.get("ShippingAddressRecipient")
    if shipping_address_recipient:
        print(
            "Shipping Address Recipient: {} has confidence: {}".format(
                shipping_address_recipient.value,
                shipping_address_recipient.confidence,
            )
        )
    print("Invoice items:")
    buxus_items = []

    if invoice.fields.get("Items"):
        for idx, item in enumerate(invoice.fields.get("Items").value) :
            print("...Item #{}".format(idx + 1))
            item_description = item.value.get("Description")
            if item_description:
                print(
                    "......Description: {} has confidence: {}".format(
                        item_description.value, item_description.confidence
                    )
                )
            item_quantity = item.value.get("Quantity")
            if item_quantity:
                print(
                    "......Quantity: {} has confidence: {}".format(
                        item_quantity.value, item_quantity.confidence
                    )
                )
            unit = item.value.get("Unit")
            if unit:
                print(
                    "......Unit: {} has confidence: {}".format(
                        unit.value, unit.confidence
                    )
                )
            unit_price = item.value.get("UnitPrice")
            if unit_price:
                print(
                    "......Unit Price: {} has confidence: {}".format(
                        unit_price.value, unit_price.confidence
                    )
                )
            product_code = item.value.get("ProductCode")
            if product_code:
                print(
                    "......Product Code: {} has confidence: {}".format(
                        product_code.value, product_code.confidence
                    )
                )
            item_date = item.value.get("Date")
            if item_date:
                print(
                    "......Date: {} has confidence: {}".format(
                        item_date.value, item_date.confidence
                    )
                )
            tax = item.value.get("Tax")
            if tax:
                print(
                    "......Tax: {} has confidence: {}".format(tax.value, tax.confidence)
                )
            amount = item.value.get("Amount")
            if amount:
                print(
                    "......Amount: {} has confidence: {}".format(
                        amount.value, amount.confidence
                    )
                )
            if item_description and regex.match('(buxus|boxwood){e<=1}', item_description.value):
                buxus_items.append({
                    'item_description': print_field(item_description),
                    'item_quantity': compute_quantity(item_quantity, amount, unit_price),
                    'unit': print_field(unit),
                    'unit_price': print_currency(unit_price),
                    'amount': print_currency(amount)
                })
    subtotal = invoice.fields.get("SubTotal")
    if subtotal:
        print(
            "Subtotal: {} has confidence: {}".format(
                subtotal.value, subtotal.confidence
            )
        )
    total_tax = invoice.fields.get("TotalTax")
    if total_tax:
        print(
            "Total Tax: {} has confidence: {}".format(
                total_tax.value, total_tax.confidence
            )
        )
    previous_unpaid_balance = invoice.fields.get("PreviousUnpaidBalance")
    if previous_unpaid_balance:
        print(
            "Previous Unpaid Balance: {} has confidence: {}".format(
                previous_unpaid_balance.value, previous_unpaid_balance.confidence
            )
        )
    amount_due = invoice.fields.get("AmountDue")
    if amount_due:
        print(
            "Amount Due: {} has confidence: {}".format(
                amount_due.value, amount_due.confidence
            )
        )
    service_start_date = invoice.fields.get("ServiceStartDate")
    if service_start_date:
        print(
            "Service Start Date: {} has confidence: {}".format(
                service_start_date.value, service_start_date.confidence
            )
        )
    service_end_date = invoice.fields.get("ServiceEndDate")
    if service_end_date:
        print(
            "Service End Date: {} has confidence: {}".format(
                service_end_date.value, service_end_date.confidence
            )
        )
    service_address = invoice.fields.get("ServiceAddress")
    if service_address:
        print(
            "Service Address: {} has confidence: {}".format(
                service_address.value, service_address.confidence
            )
        )
    service_address_recipient = invoice.fields.get("ServiceAddressRecipient")
    if service_address_recipient:
        print(
            "Service Address Recipient: {} has confidence: {}".format(
                service_address_recipient.value,
                service_address_recipient.confidence,
            )
        )
    remittance_address = invoice.fields.get("RemittanceAddress")
    if remittance_address:
        print(
            "Remittance Address: {} has confidence: {}".format(
                remittance_address.value, remittance_address.confidence
            )
        )
    remittance_address_recipient = invoice.fields.get("RemittanceAddressRecipient")
    if remittance_address_recipient:
        print(
            "Remittance Address Recipient: {} has confidence: {}".format(
                remittance_address_recipient.value,
                remittance_address_recipient.confidence,
            )
        )
    if customer_name:
        customer_name_value = customer_name.value
    else:
        customer_name_value = None
    return {
        'customer_name': customer_name_value,
        'customer_address': print_address_value(customer_address),
        'shipping_address': print_address_value(shipping_address),
        'shipping_address_recipient': print_field(shipping_address_recipient),
        'date': print_date_value(invoice_date or service_end_date or due_date),
        'buxus_items': buxus_items
    }

def compute_quantity(item_quantity, amount, unit_price):
    if item_quantity and item_quantity.value:
        return int(item_quantity.value)
    else:
        if amount and amount.value and unit_price and unit_price.value:
            return int(print_currency(amount) / print_currency(unit_price))

def print_field(field):
    if field:
        return field.value

def print_date_value(date):
    if date and date.value:
        return date.value.isoformat()

def print_currency(currency):
    if currency and currency.value:
        return currency.value.amount

def print_address_value(address):
    if address and address.value:
        address_value = address.value
        fieldnames = ['street_address', 'city', 'state', 'postal_code']
        return ' '.join(filter(None, [getattr(address.value, fieldname) for fieldname in fieldnames if fieldname]))

def item_quantity_selector(item):
    if item['item_quantity']:
        return item['item_quantity']
    return 0

def print_invoices(filename, invoices, selected_extracts):
    for idx, invoice in enumerate(invoices.documents):
        extract = print_invoice(idx, invoice)
        extract['filename'] = filename
        extract['buxus_count'] = sum(map(item_quantity_selector, extract['buxus_items']))
        selected_extracts.append(extract)

if __name__ == "__main__":
    source_dir = 'data/pages/'
    # filelist = ['NFLD-001.pdf.pickle']
    filelist = os.listdir(source_dir)
    selected_extracts = []
    for input in filelist:
        if not input.endswith('.pickle'):
            continue
        input_fullpath = os.path.join(source_dir, input)
        print(input_fullpath)
        with open(input_fullpath, 'rb') as picklefile:
            invoices = pickle.load(picklefile)
        print_invoices(input, invoices, selected_extracts)
        print(selected_extracts)
    with open('postprocess.json', 'w+') as f:
        json.dump(selected_extracts, f)