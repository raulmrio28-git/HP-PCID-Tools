# Unofficial HP PCID Tools
I decided to create these Python tools designed to decode (and in the future, encode) HP/Compaq PCID values used in notebooks/laptops during 2008-2014.

# NOTICE
Before using the following tool, you'll accept and are resposible that you might break confidentiality terms of HP themselves (the ones behind the PCID format and values used). I and the user will NOT be responsible for any damages caused by the creation, research and usage of this tool. 

# What is a PCID?
PCID in short stands for Product Configuration ID, used to store flags for software and hardware customizations during factory preinstallation of OS and software. This string was introduced in around 2008 and used up until 2014 when they switched the method to the 2-digit Feature Byte(s) and Build ID initially used on desktops (also known in their lingo as "Fusion").

# Where do I find the PCID?
The PCID text can be found mainly on the back of the notebook/laptop, usually on a label on the back cover or under battery bay.

# What's the purpose of the tools?
1. pcid_read - Decode PCID values into user-understandable information
2. pcid_write (not done yet) - Encode PCID values from user input

# Sources used
- TDC EEPROM Utility UI Specification (cannot provide document here as it's marked confidential, but can be found in packages for NBDMIFit)
