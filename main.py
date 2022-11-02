import speedtest
import csv
import datetime

x = datetime.datetime.now()
st = speedtest.Speedtest()

# convert bytes ke MB
def bytes_ke_megaBytes(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes/MB)

ds = bytes_ke_megaBytes(st.download())
us = bytes_ke_megaBytes(st.upload())

print("Download speed : ", ds, "Mbps")
print("Upload speed : ", us, "Mbps")


# csv header
fieldnames = ['dates', 'Upload_Mbps', 'Download_Mbps']

# csv data
rows = [
    {'dates': x.strftime("%c"),
    'Upload_Mbps': us,
    'Download_Mbps': ds}
    
]

with open('speed.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

