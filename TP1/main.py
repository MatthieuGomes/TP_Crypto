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

def testing_long_message():
    long_message=b"""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"""
    md5_hash = hash_md5(long_message)
    sha1_hash = hash_sha1(long_message)
    print(f"Long Message Test:{long_message}")  # Print only the beginning of the long message
    print(f"MD5: {md5_hash}")
    print(f"SHA1: {sha1_hash}")



if __name__ == "__main__":
    # Example usage
    testing_hash_functions()
    testing_long_message()
# TP Crypto --- IGNORE ---