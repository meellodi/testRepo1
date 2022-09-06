def defangIPaddr(address):
    def defangIPaddrRecursive(chunk):
        if len(chunk) == 1:
            if chunk == ".":
                return "[.]"
            else:
                return chunk
        else:
            return defangIPaddrRecursive(chunk[:1])+defangIPaddrRecursive(chunk[1:])

    return defangIPaddrRecursive(address)


print(defangIPaddr("."))
print(defangIPaddr(".."))
print(defangIPaddr("1"))
print(defangIPaddr("1.1.1.1"))
# defangIPaddr("255.100.50.0")
