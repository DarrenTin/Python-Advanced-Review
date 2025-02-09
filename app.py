import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import pandas as pd

# Twilio credentials
TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_WHATSAPP_NUMBER = "whatsapp:+"
MY_WHATSAPP_NUMBER = "whatsapp:+"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def generate_invoice_text(df):
    """Generate invoice as a text message."""
    invoice_text = "Invoice:\n"
    invoice_text += "{:<5} {:<20} {:<10} {:<5} {:<10}\n".format("No", "Item", "Price", "Qty", "Total")
    
    for _, row in df.iterrows():
        invoice_text += "{:<5} {:<20} ${:<10.2f} {:<5} ${:<10.2f}\n".format(
            row["No"], row["Item"], row["Price"], row["Qty"], row["Total"]
        )
    
    subtotal = df["Total"].sum()
    tax = subtotal * 0.1
    total = subtotal + tax

    invoice_text += "\nSubtotal: ${:.2f}".format(subtotal)
    invoice_text += "\nTotal (10% tax): ${:.2f}".format(total)
    
    return invoice_text

def handle_message(message):
    """Process the user's input to generate an invoice."""
    rows = []
    for line in message.split("\n"):
        item, price, qty = line.split(",")
        rows.append({
            "No": len(rows) + 1,
            "Item": item.strip(),
            "Price": float(price.strip()),
            "Qty": int(qty.strip()),
            "Total": float(price.strip()) * int(qty.strip())
        })

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(rows)

    # Generate the invoice text
    invoice_text = generate_invoice_text(df)
    return invoice_text

def send_invoice_text(invoice_text, to_whatsapp_number):
    """Send the generated invoice as a text message to the user."""
    message = client.messages.create(
        body=invoice_text,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=to_whatsapp_number
    )
    return message

# Flask Webhook to receive WhatsApp messages (requires Flask for webhooks)

from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    """Handle incoming WhatsApp messages and reply with a text invoice."""
    incoming_msg = request.form.get('Body', '')
    sender = request.form.get('From', '')

    if incoming_msg:
        # Generate invoice based on the message content
        invoice_text = handle_message(incoming_msg)

        # Send the invoice text back to the user
        send_invoice_text(invoice_text, sender)

        # Reply to acknowledge receipt of the message
        resp = MessagingResponse()
        resp.message("Your invoice is being generated and will be sent shortly.")
        return str(resp)
    
    return "No message received", 400

if __name__ == "__main__":
    app.run(debug=True)
