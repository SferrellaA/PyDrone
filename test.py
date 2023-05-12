import pyrcrack

# so pycrack is just outright not supported on windows
# and I couldn't make it work without rewriting the whole thing
# on the pi it is then

import os
os.environ["SKIP_ROOT_CHECK"] = "1"
print(os.getenv("SKIP_ROOT_CHECK"))

airmon = pyrcrack.AirmonNg()
print(airmon.interfaces)