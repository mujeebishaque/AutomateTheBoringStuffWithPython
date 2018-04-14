import requests

response = requests.get('url')

result = response.status_code

# suppose we got text from web_page,So now
#  let's save it in b mode

file = open('someFile.txt', 'wb')
# wb => write binary

for chunk in response.iter_content(10000):
    # iter_content returns chunk of data in bytes.
    # pass the num of bytes per iter in method above.
    file.write(chunk)

file.close()

"""
raise_for_status() raises an exception

if result == 400 or result == 404:
    pass
else:
    # save the file
    pass
better to use try and catch
"""