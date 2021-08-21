from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/poseidon"

page = urlopen(url)

print(page)

html_bytes = page.read()
html = html_bytes.decode('utf-8')
print(html)

# extrating info using strings :-

head_index = html.find('<title >')
print(head_index)

start_index = head_index + len('<title >')
print(start_index)

end_index = html.find('</title>')
print(end_index)

title= html[start_index:end_index]
print(title)
