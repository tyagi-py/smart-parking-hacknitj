import os
from tempfile import NamedTemporaryFile
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
from datetime import datetime
from time import time

# choose english as language
def gen_receipt(car_no='HR 02 AK 9064',mins = 50):
    os.environ["INVOICE_LANG"] = "en"
    client = Client("R/C Number: "+car_no)
    provider = Provider('Tez Parking', bank_account='2600420569', bank_code='2010',address='Tez Parking\n NIT Jalandhar', city='Jalandhar\n Punjab', zip_code='144001', phone='9138121216', email='sumittyagi1998@gmail.com',  logo_filename='think.png')
    creator = Creator('Parking Operator')
    now = time()
    now = int(now)
    now = str(now)
    invoice = Invoice(client, provider, creator)
    invoice.currency_locale = 'en_US.UTF-8'
    rate =0.5
    if mins <= 60:
        rate = 20/60
    elif mins >60 and mins <= 180:
        rate = 40/60
    elif mins > 180 and mins <=300:
        rate = 50/60
    elif mins > 300 and mins <= 480:
        rate = 60/60
    elif mins > 480 and mins <= 720:
        rate = 80/60
    elif mins > 720 and mins <= 1440:
        rate = 100/60

    invoice_no = now+car_no[-4:]
    invoice.add_item(Item(mins, rate, description="Parking slot booking"))
    invoice.number = invoice_no

    pdf = SimpleInvoice(invoice)
    pdf.gen(invoice_no+".pdf", generate_qr_code=True)
    return invoice_no



