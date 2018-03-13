import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Dataset
deskphone_count = 999
third_party_sip_count = 100
conference_phone_count = 88
analog_count = 400
wireless_phone_count = 700
softphone_count = 566

# Turn dataset int oa dictionary
phone_counts = {"Desk Pbones": deskphone_count, "Conference Phones": conference_phone_count, "Analog": analog_count, "Wireless Phones": wireless_phone_count, "Softphones": softphone_count}

# Create a sorted list of the dictionary values
phone_quantities = sorted(phone_counts.values())
phone_category_labels = []

# Sort labels and create separate label list in matching order with value list
for phone in phone_quantities:
    for name, number in phone_counts.iteritems():
        if phone == number:
            phone_category_labels.append(name)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
PP = PdfPages('multipage.pdf')

fig1, ax1 = plt.subplots()
ax1.pie(phone_quantities, labels=phone_category_labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig(PP, format='pdf')
