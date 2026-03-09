



'''
    Information based on the "TDC EEPROM Utility UI Specification" document Rev 4.6
'''

import sys
import os

KbType =\
    {
        0: "Standard", 
        1: "Japanese",
        2: "EMEA/UK",
        3: "Brazil"
    }
CleanImageType =\
    {
        0: "Normal", 
        1: "Clean"
    }
TPMFlag =\
    {
        0: "Disabled", 
        1: "Enabled"
    }
ChannelID =\
    {
        "00":"Generic BTO/CTO",
        "01":"HP CTO",
        "02":"Best Buy",
        "03":"Walmart",
        "04":"MTV/Youth Special Edition",
        "05":"Carphone Warehouse (UK)",
        "06":"TIM (Italy)",
        "07":"Telefónica (Spain; Latin-America)",
        "08":"Vodafone (Pan-European)",
        "09":"Orange",
        "0A":"Best Buy Photo",
        "0B":"Verizon",
        "0C":"Radio Shack",
        "0D":"T-Mobile",
        "0E":"China Mobile",
        "0F":"China Telecom",
        "10":"China Unicom",
        "11":"Beats Special Edition",
        "12":"APJ",
        "13":"Vodafone",
        "14":"Costco",
        "15":"Rossignol",
        "16":"Recyclic Cycle Specific Channel ID #1",
        "17":"Recyclic Cycle Specific Channel ID #2",
        "18":"Recyclic Cycle Specific Channel ID #3",
        "19":"Recyclic Cycle Specific Channel ID #4",
        "1A":"Recyclic Cycle Specific Channel ID #5",
        "1B":"Recyclic Cycle Specific Channel ID #6",
        "1C":"Recyclic Cycle Specific Channel ID #7",
        "1D":"Recyclic Cycle Specific Channel ID #8",
        "1E":"Recyclic Cycle Specific Channel ID #9",
        "1F":"Recyclic Cycle Specific Channel ID #10",
        "20":"Call of Duty",
        "21":"Sam’s Club",
        "22":"Best Buy Premium Collection",
        "23":"FNAC",
        "24":"Microsoft Signature"
    }
OSSKU = \
    {
        0:"Non-Windows",
        1:"Windows Vista",
        2:"Windows 7",
        3:"Windows 8",
        4:"Windows 8.1",
        5:"non-Windows UEFI OS"
    }
QuickPlay = \
    {
        0:"DVDP",
        1:"DVDP and QP4W",
        4:"MediaSmart without Instant On",
        5:"MediaSmart with Instant On"
    }
Wallpapers = \
    {
        "00":"Default",
        "01":"Wave (Pavilion IMR1)",
        "02":"Digicode (Presario IMR1)",
        "03":"OTC (OrderToChaos)",
        "04":"Radiance (Pavilion IMR2)",
        "05":"Trace (Presario IMR2)",
        "06":"Organic",
        "07":"Dragon (HDX 9000)",
        "08":"Sputnik 1.2",
        "09":"Sprout (SE#5)",
        "0A":"Youth Edition (MTV)",
        "0B":"Grid (Diablo 1.0)",
        "0C":"2C08 PA Corlab Wallpapers",
        "0D":"2C08 PR Corlab Wallpapers",
        "0E":"3C08 PA Bronze",
        "0F":"Titanium (HDX)",
        "10":"BBYSE (Mysterious Waves)",
        "11":"CCYSE (Fall Leaves)",
        "12":"1.5C09 Black Gold",
        "13":"1.5C09 Moonlight Chrome",
        "14":"1C09 tx2 Reaction",
        "15":"2C09 Modern Vintage",
        "16":"2C09 China Mobile",
        "17":"2C09 MTV 2.0",
        "18":"2C09 Best Buy NextClass",
        "19":"3C09 Envy Stardock",
        "1A":"Beats Special Edition",
        "1B":"3C09 HP Mini",
        "1C":"3C09 CPQ Mini",
        "1D":"3C09 SE Mini",
        "1E":"3C09 HP Mini Pink",
        "1F":"CityLight",
        "20":"1C10 HP Mini Silver",
        "21":"1C10 HP Mini Black",
        "22":"1C10 HP Mini Red",
        "23":"1C10 HP Mini Blue",
        "24":"1C10 CPQ Mini Black",
        "25":"1C10 HP Mini Special 1",
        "26":"1C10 CPQ Mini Special 2",
        "27":"1C10 OPP MUSE HPG",
        "28":"1C10 OPP MUSE Presario",
        "29":"2C10 Akashi",
        "2A":"Riptide",
        "2B":"City Wires",
        "2C":"Birds Land",
        "2D":"Freebirds",
        "2E":"After the rain",
        "2F":"Grow",
        "30":"Sunset Fox",
        "31":"Alpine Tundra",
        "32":"City Rooftops",
        "33":"City Corner",
        "34":"Coffee Shop",
        "35":"Bookstore",
        "36":"Bakery",
        "37":"Athos",
        "38":"Porthos",
        "39":"Aramis",
        "3A":"Free Birds Lavender Frost",
        "3B":"Free Birds Luminous Rose",
        "3C":"3C10 Wal-Mart SE",
        "3D":"Wallpaper #1 for SE (Re-cyclic)",
        "3E":"Wallpaper #2 for SE (Re-cyclic)",
        "3F":"Wallpaper #3 for SE (Re-cyclic)",
        "40":"Wallpaper #4 for SE (Re-cyclic)",
        "41":"Wallpaper #5 for SE (Re-cyclic)",
        "42":"Renewal",
        "43":"Hope",
        "44":"Carnival",
        "45":"Songkran",
        "46":"Arrival",
        "47":"Paeonia",
        "48":"Finesse (ENVY)",
        "49":"Persica",
        "4A":"Calluna",
        "4B":"Architect",
        "4C":"Aggregate",
        "4D":"MATO",
        "4E":"Ilos",
        "4F":"Herchcovitch, Alexandre",
        "50":"Adrift",
        "51":"Don't Let Go",
        "52":"Elephant Parade",
        "53":"Fish Feast",
        "54":"Harvest",
        "55":"In the Deep",
        "56":"Not Alone",
        "57":"Keeper",
        "58":"Weightless Fire",
        "59":"Svinøya Sunset",
        "5A":"No Smoke Without Fire",
        "5B":"Orkney Stones",
        "5C":"Catalina Park",
        "5D":"Washing Up Time",
        "5E":"Make it Matter",
        "5F":"Make it Matter (Rango)",
        "60":"3C14 Gaming"
    }
BurningSW = \
    {
       0: "Free Version",
       1: "Main Stream Version",
       2: "High-End Version"
    }
WWAN = \
    {
        0:"No Carrier Preference (Default)",
        1:"Carrier/Carrier Group 1 (Verizon)",
        2:"Carrier/Carrier Group 2 (AT&T)",
        3:"Carrier/Carrier Group 3 (Sprint)",
        4:"Carrier/Carrier Group 4 (Verizon, Sprint and AT&T)"
    }
WWANIntAntenna = \
    {
        0:"No",
        1:"Yes"
    }
GPSCapableAntenna = \
    {
        0:"No",
        1:"Yes"
    }
OSSubVersion = \
    {
        0:"Standard",
        1:"SST",
        2:"NA High Volume",
        3:"NA",
        4:"NA EM",
        5:"Connected (w/ Bing)",
        6:"Educational (Student)",
        7:"Connected (w/ Bing for Tablets)",
        8:"Connected (w/ Bing for Small Tablets)",
        9:"Connected (w/ Bing and Office 365 for Tablets)",
        10:"Connected (w/ Bing and Office 365 for Small Tablets)"
    }
MediaSmart = \
    {
        0:"MediaSmart",
        1:"MediaSmart Premium",
        2:"MediaSmart Life"
    }
ODD = \
    {
        0:"System with Internal LightScribe ODD (DVD/BD)",
        1:"System bundled with external LightScribe ODD (DVD)",
        2:"System bundled with external LightScribe ODD (BD)",
        3:"System without ODD",
        4:"System bundled with external non-LightScribe ODD (DVD)",
        5:"System bundled with external non-LightScribe ODD (BD)",
        6:"System with Internal non-LightScribe ODD (DVD/BD)"
    }
WinSKU7 = \
    {
        0:"Starter",
        1:"Home Basic",
        2:"Home Premium",
        3:"Professional",
        4:"Ultimate",
    }
WinSKU8 = \
    {
        0:"China",
        1:"Single Language (SL)",
        2:"Core",
        3:"Professional",
        4:"China w/Bing",
        5:"Single Language (SL) w/Bing",
        6:"Core w/Bing",
        7:"Professional for Student",
    }
ImageID = \
    {
        0:"Standard",
        1:"SMB",
        2:"WiMax",
        3:"Beats",
        4:"Windows 7 Downgrade",
        5:"Ubuntu Kylin"
    }
EnergyStar = \
    {
        0:"No",
        1:"Yes"
    }
Ultrabook = \
    {
        0:"No",
        1:"Yes"
    }
HPBrandCPU = \
    {
        0:"No",
        1:"Yes"
    }
NIS = \
    {
        0:"Symantec NIS 60 Day Subscription",
        1:"Symantec NIS 60 Day Subscription SMB",
        2:"Symantec NIS 180 Day Subscription",
        3:"Symantec NIS 12 Month Subscription",
        4:"Symantec NIS 15 Month Subscription",
        5:"Symantec NIS 24 Month Subscription (Premium)",
        6:"Symantec NIS 24 Month Subscription",
        7:"Symantec NIS 36 Month Subscription",
        8:"None"
    }
McAfee = \
    {
        0:"McAfee 30 Day Subscription",
        1:"McAfee 30 Day Subscription SMB",
        2:"McAfee 180 Day Subscription",
        3:"McAfee 12 Month Subscription",
        4:"McAfee 12 Month Subscription (Premium)",
        5:"McAfee 24 Month Subscription",
        6:"McAfee 24 Month Subscription",
        7:"None"
    }
Office = \
    {
        0:"Non-AFO",
        1:"AFO"
    }

'''
    Taken from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
'''

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def we_are_in_windows():
    if sys.platform == "win32":
        return True
    else:
        return False

def pcid_checksum(str):
    idx = 0
    sum = 0
    for idx in range(25):
        if idx != 2 and idx != 3:
            sum = (sum+ord(str[idx]))&0xff
    
    return ((~sum)+1)&0xff

def pcid_decode(str):
    if we_are_in_windows() == True:
        os.system('color') #fix printing colors
    print(f"PCID input:\n\t{str}")
    version = int(str[:2], 16)
    print(f"Version:\n\t{version}")
    if version >=3:
        checksum = str[2:4]
        actual_pcid = str[4:]
    else:
        checksum = "Not supported in this version"
        actual_pcid = str[2:]
    if checksum != "Not supported in this version":
        checksum_int = int(checksum, 16)
        checksum_calc = pcid_checksum(str)
        if checksum_int != checksum_calc:
            chk_calcresult = f"-> {bcolors.FAIL}INVALID checksum{bcolors.ENDC}"
        else:
            chk_calcresult = f"-> {bcolors.OKGREEN}VALID checksum{bcolors.ENDC}"
        print(f"Checksum:\n\t{checksum} {chk_calcresult}")
    plat_revision = actual_pcid[0:3]
    print(f"Platform Revision:\n\t{plat_revision}")
    cfg_byte = int(actual_pcid[3], 16)
    kb_type = KbType.get((cfg_byte&1) | (((cfg_byte>>3)&1)<<1), "Unknown")
    print(f"Keyboard Type:\n\t{kb_type}")
    clean_image = CleanImageType.get(((cfg_byte>>1)&1), "Unknown")
    print(f"Clean Image Type:\n\t{clean_image}")
    tpm = TPMFlag.get(((cfg_byte>>2)&1), "Unknown")
    print(f"TPM Flag:\n\t{tpm}")
    channel = ChannelID.get(actual_pcid[4:6], "Unknown")
    print(f"Channel ID:\n\t{channel}")
    os_sku_dec = int(actual_pcid[6], 16)
    os_sku = OSSKU.get(os_sku_dec, "Unknown")
    print(f"OS SKU:\n\t{os_sku}")
    quickplay = QuickPlay.get(int(actual_pcid[7], 16), "Unknown")
    print(f"QuickPlay flag:\n\t{quickplay}")
    wallpaper = Wallpapers.get(actual_pcid[8:10], "Unknown")
    print(f"Wallpaper:\n\t{wallpaper}")
    data_burn_sw_version = BurningSW.get(int(actual_pcid[10], 16), "Unknown")
    print(f"Data Burn SW Version:\n\t{data_burn_sw_version}")
    wwan_carrier = WWAN.get(int(actual_pcid[11], 16), "Unknown")
    print(f"WWAN Carrier:\n\t{wwan_carrier}")
    wwan_antenna = WWANIntAntenna.get(int(actual_pcid[12], 16), "Unknown")
    print(f"WWAN Antenna:\n\t{wwan_antenna}")
    if version == 9:
        os_subversion = OSSubVersion.get(int(actual_pcid[14], 16), "Unknown")
        print(f"OS Sub-version:\n\t{os_subversion}")
    else:
        gps_antenna = GPSCapableAntenna.get(int(actual_pcid[13], 16), "Unknown")
        print(f"GPS Antenna:\n\t{gps_antenna}")
    actual_pcid = actual_pcid[14:]
    mediasmart = MediaSmart.get(int(actual_pcid[0], 16), "Unknown")
    print(f"MediaSmart Flag:\n\t{mediasmart}")
    if version >= 2:
        odd =  ODD.get(int(actual_pcid[1], 16), "Unknown")
        print(f"ODD (Optical Disc Drive) Configuration:\n\t{odd}")
        actual_pcid = actual_pcid[2:]
    if version >= 3:
        if os_sku_dec >= 3 and os_sku_dec < 5:
            win_cfg = WinSKU8.get(int(actual_pcid[0], 16), "Unknown")
        elif os_sku_dec >= 1 and os_sku_dec < 3:
            win_cfg = WinSKU7.get(int(actual_pcid[0], 16), "Unknown")
        else:
            win_cfg = "None"
        print(f"Windows Edition:\n\t{win_cfg}")
        actual_pcid = actual_pcid[1:]
    if version >= 4:
        img_id =  ImageID.get(int(actual_pcid[0], 16), "Unknown")
        print(f"Image ID:\n\t{img_id}")
        actual_pcid = actual_pcid[1:]
    if version >= 5:
        cfg_byte2 =  int(actual_pcid[0], 16)
        estar = EnergyStar.get(cfg_byte2&1, "Unknown")
        print(f"Energy Star:\n\t{estar}")
        if version == 9:
            ubook = Ultrabook.get((cfg_byte2>>1)&1, "Unknown")
            print(f"Ultrabook:\n\t{ubook}")
            hpcpu = HPBrandCPU.get((cfg_byte2>>2)&1, "Unknown")
            print(f"HP Branding CPU:\n\t{hpcpu}")
            office = Office.get((cfg_byte2>>3)&1, "Unknown")
            print(f"Office:\n\t{office}")
        actual_pcid = actual_pcid[1:]
    if version >= 8:
        nis = NIS.get(int(actual_pcid[0], 16), "Unknown")
        print(f"Symantec NIS:\n\t{nis}")
        actual_pcid = actual_pcid[1:]
    if version == 9:
        mcafee = McAfee.get(int(actual_pcid[0], 16), "Unknown")
        print(f"McAfee:\n\t{mcafee}")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"No PCID input!\nUsage:\n\t{sys.argv[0]} <PCID>")
        sys.exit(1)
    pcid = sys.argv[1]
    pcid_decode(pcid)