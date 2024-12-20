PDU_Table = [
"ADV_IND",
"ADV_DIRECT_IND",
"ADV_NONCONN_IND",
"SCAN_REQ",
"SCAN_RSP",
"CONNECT_IND",
"ADV_SCAN_IND",
"ADV_EXT_IND",
"AUX_CONNECT_RSP"
] # only primary advertising channels

GAP_Table = {
0x01:
"Flags",

0x02:
"Incomplete List of 16­bit Service Class UUIDs",

0x03:
"Complete List of 16­bit Service Class UUIDs",

0x04:
"Incomplete List of 32­bit Service Class UUIDs",

0x05:
"Complete List of 32­bit Service Class UUIDs",

0x06:
"Incomplete List of 128­bit Service Class UUIDs",

0x07:
"Complete List of 128­bit Service Class UUIDs",

0x08:
"Shortened Local Name",

0x09:
"Complete Local Name",

0x0A:
"Tx Power Level",

0x0D:
"Class of Device",

0x0E:
"Simple Pairing Hash C­192",

0x0F:
"Simple Pairing Randomizer R­192",

0x10:
"Device ID or Security Manager TK Value",

0x11:
"Security Manager Out of Band Flags",

0x12:
"Peripheral Connection Interval Range",

0x14:
"List of 16­bit Service Solicitation UUIDs",

0x15:
"List of 128­bit Service Solicitation UUIDs",

0x16:
"Service Data ­ 16­bit UUID",

0x17:
"Public Target Address",

0x18:
"Random Target Address",

0x19:
"Appearance",

0x1A:
"Advertising Interval",

0x1B:
"LE Bluetooth Device Address",

0x1C:
"LE Role",

0x1D:
"Simple Pairing Hash C­256",

0x1E:
"Simple Pairing Randomizer R­256",

0x1F:
"List of 32­bit Service Solicitation UUIDs",

0x20:
"Service Data ­ 32­bit UUID",

0x21:
"Service Data ­ 128­bit UUID",

0x22:
"LE Secure Connections Confirmation Value",

0x23:
"LE Secure Connections Random Value",

0x24:
"URI",

0x25:
"Indoor Positioning",

0x26:
"Transport Discovery Data",

0x27:
"LE Supported Features",

0x28:
"Channel Map Update Indication",

0x29:
"PB­ADV",

0x2A:
"Mesh Message",

0x2B:
"Mesh Beacon",

0x2C:
"BIGInfo",

0x2D:
"Broadcast_Code",

0x2E:
"Resolvable Set Identifier",

0x2F:
"Advertising Interval ­- long",

0x30:
"Broadcast_Name",

0x3D:
"3D Information Data",

0x31:
"Encrypted Advertising Data",

0x32:
"Periodic Advertising Response Timing Information",

0xFF:
"Manufacturer Specific Data"
}


def PDU_Lookup(code):
	if code > 0b1000: return "RFU"
	return PDU_Table[code]

def GAP_Lookup(code):
	# using a dict here because the numbers aren't contiguous
	return GAP_Table.get(code, "%s Not In Lookup Table" % hex(code))