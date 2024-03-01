import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext('Screenshot 2024-02-29 211938.png', detail = 0)
print(result)