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

def testing_hash_functions():
    test_messages = [b"ENSEA", b"eNSEA", b"eNSeA", b"EN5EA"]
    for msg in test_messages:
        md5_hash = hash_md5(msg)
        sha1_hash = hash_sha1(msg)
        print(f"Message: {msg}")
        print(f"MD5: {md5_hash}")
        print(f"SHA1: {sha1_hash}")
        print("-" * 30)

if __name__ == "__main__":
    # Example usage
    testing_hash_functions()
# TP Crypto --- IGNORE ---