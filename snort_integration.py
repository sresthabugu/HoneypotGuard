import snortlib

def send_to_snort(packet):
    snort = snortlib.Snort()
    snort.alert(packet)
