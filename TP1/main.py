from Crypto.Hash import MD5,SHA1

def hash_md5(data):
    """
    Hashes the input data using MD5.
    
    :param data: The input data to hash.
    :return: The MD5 hash of the input data.
    """
    h = MD5.new()
    h.update(data)
    return h.hexdigest()

def hash_sha1(data):
    """
    Hashes the input data using SHA1.
    
    :param data: The input data to hash.
    :return: The SHA1 hash of the input data.
    """
    h = SHA1.new()
    h.update(data)
    return h.hexdigest()

if __name__ == "__main__":
    # Example usage
    msg_list = [b"ENSEA", b"eNSEA", b"eNSeA", b"EN5EA"]
    for msg in msg_list:
        print(f"Message: {msg}")
        print("MD5:", hash_md5(msg))
        print("SHA1:", hash_sha1(msg))
# TP Crypto --- IGNORE ---