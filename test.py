import asyncio

import pyrcrack

from rich.console import Console

from time import time

async def scan_for_targets(start, length):
    """Scan for targets, return json."""
    console = Console()
    airmon = pyrcrack.AirmonNg()

    interface = "wlan1"
    for i in await airmon.interfaces:
        print(f'Available: {i}')

    async with airmon(interface) as mon:
        async with pyrcrack.AirodumpNg() as pdump:
            async for result in pdump(mon.monitor_interface):
                #Essid, Bssid, Packets, Dbm, Score, Channel, Encryption
                #console.print(result.table)
                #print(result.table.columns[0].header) # 'Essid'
                #print(result.table.rows)
                print(result.table.columns)

                '''
                wtf? pyrcrack just actually doesn't let you configure anything
                This is totally useless
                Also only returning things in rich table format is pretty useless
                '''

                if time() - start  >= length:
                    break

print("Starting")
asyncio.run(scan_for_targets(time(), 5))
print("Done")