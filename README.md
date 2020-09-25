# HTTPStatusCodes
HTTPStatusCodes returns a string detailing of what a given status code means.

## Install
Pip coming soon.
## How to use
```py
from HTTPStatusCodes import get_status_string
status = get_status_string(200)
print (status)
>>> 'OK'
```
Alternatively 
```py
import HTTPStatusCodes
status = HTTPStatusCodes.get_status_string(200)
print(status)
>>> 'OK'
```
