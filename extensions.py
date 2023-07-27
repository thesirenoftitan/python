filename = input("File name: \n").strip()  # remove leading and trailing spaces
extension = filename.split('.')[-1].lower()  # convert to lowercase

if extension == 'gif':
    print("image/gif")

elif extension == 'jpg' or extension == 'jpeg':
    print("image/jpeg")

elif extension == 'png':
    print("image/png")

elif extension == 'pdf':
    print("application/pdf")

elif extension == 'txt':
    print("text/plain")

elif extension == 'zip':
    print("application/zip")

else:
    print("application/octet-stream")
