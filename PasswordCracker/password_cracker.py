import hashlib
import sys
# # Creating a test hash for the password "password123"
# test_password = "password123"
# test_hash = hashlib.md5(test_password.encode()).hexdigest()
# print(f"MD5 hash of '{test_password}': {test_hash}")

def create_test_hashes():
    """
    Create multiple test hashes for the cracking practice
    """
    test_passwords = ["password123", "admin", "123456", "qwerty", "letmein"]
    
    print("Creating test hashes:")
    print("-" * 50)
    
    for password in test_passwords:
        hash_value = hashlib.md5(password.encode()).hexdigest()
        print(f"Password: {password:12} Hash: {hash_value}"  )

def save_target_hashes():
    """
    Save our test hashes to a file for cracking practice
    """
    test_passwords = ["password123", "admin", "123456", "qwerty", "letmein"]
    
    with open("target_hashes.txt", "w") as file:
        file.write("# MD5 hashes for password cracking practice\n")
        file.write("# Format: hash_value\n\n")
        
        for password in test_passwords:
            hash_value = hashlib.md5(password.encode()).hexdigest()
            file.write(f"{hash_value}\n")
            
    print("Target hashes saved to target_hashes.txt")

def create_wordlist():
    """Create a basic wordlist for dictionary attacks"""
    common_passwords = [
        "password123", "123456", "password", "admin", "qwerty",
        "letmein", "welcome", "monkey", "dragon", "master",
        "123456789", "football", "baseball", "abc123", "superman"
    ]
    
    with open("common_passwords.txt", "w") as file:
        for password in common_passwords:
            file.write(f"{password}\n")
            
    print("Wordlist saved to common_passwords.txt")
    
def crack_single_hash(target_hash, wordlist_file):
    """
    Attempt to crack a single MD5 hash using dictionary attack

    Args:
        target_hash (str): The MD5 hash we're trying to crack
        wordlist_file (str): Path to the wordlist file
        
    Returns:
        tuple: (success_bool, cracked_password, attempts_made)
    """
    
    print(f"Attempting to crack hash: {target_hash}")
    print(f"Using wordlist: {wordlist_file}")
    print("-" * 60)
    
    attempts = 0
    
    try:
        with open(wordlist_file, 'r') as file:
            for password in file:
                password = password.strip() 
                attempts += 1
                
                # Generate MD5 hash of current password attempt
                candidate_hash = hashlib.md5(password.encode()).hexdigest()
                
                # Compare against our target hash
                if candidate_hash == target_hash:
                    print(f"EUREKA! Hash cracked in {attempts} attempts")
                    print(f"Password found: {password}")
                    return True, password, attempts
                
                # Show progress every 5 attempts (since we have small wordlist)
                if attempts % 5 == 0:
                    print(f"Tested {attempts} passwords...")
            
    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist_file}' not found")
        return False, None, attempts
    
    print(f"Failed to crack hash after {attempts} attempts")
    return False, None, attempts

def test_crack_known_hash():
    """Test our cracking function against a known hash
    """
    
    target = "482c811da5d5b4bc6d497ffa98491e38"
    
    print("TESTING DICTIONARY ATTACK")
    print("=" * 50)
    
    success, password, attempts = crack_single_hash(target, "common_passwords.txt")
    
    if success:
        print(f"\nCracking Results:")
        print(f"\nTarget hash: {target}")
        print(f"Cracked password: {password}")
        print(f"Total attempts: {attempts} attempts")
    else:
        print(f"\nCracking failed after {attempts} attempts")

def crack_all_targets():
    """Attempt to crack all target hashes from our file"""
    
    # Read all target hashes from file
    target_hashes = []
    with open("target_hashes.txt", 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"): # Im skipping empty lines and comments
                target_hashes.append(line)    
                
    print("CRACKING ALL TARGET HASHES")
    print("=" * 50) 
    
    results = []
    
    for i, target_hash in enumerate(target_hashes, 1):
        print(f"\nTarget {i}/{len(target_hashes)}: {target_hash}")
        success, password, attempts = crack_single_hash(target_hash, "common_passwords.txt")
        results.append((target_hash, success, password, attempts))
        
    # A summary report 
    print("\n" + "=" * 50)
    print("FINAL RESULTS SUMMARY")
    print("=" * 50)
    successful = 0
    for target_hash, success, password, attempts in results:
        if success:
            print(f"SUCCESS {target_hash[:16]}... Password: '{password}' Attempts: {attempts}")
            successful += 1
        else:
            print(f"FAILED {target_hash[:16]}... NOT FOUND Attempts: {attempts}")
            
    print(f"\n Success Rate: {successful} out of {len(results)} total ({successful/len(results)*100:.1f}%)")
    
def timed_crack_test():
    """Test cracking with timing analysis"""
    import time
    
    target_hash = "482c811da5d5b4bc6d497ffa98491e38"  # password123
    
    print("PERFORMANCE TIMING TEST")
    print("=" * 40)
    
    start_time = time.time()
    success, password, attempts = crack_single_hash(target_hash, "common_passwords.txt")
    end_time = time.time()
    
    duration = end_time - start_time
    
    if success:
        print(f"\nPerformance Results:")
        print(f"Password: {password}")
        print(f"Attempts: {attempts}")
        print(f"Duration: {duration:.6f} seconds")
        print(f"Speed: {attempts/duration:.0f} attempts per second")
        
        
def main():
    """Main function with command line interface"""
    if len(sys.argv) != 3:
        print("Password Cracker v1.0 - MD5 Dictionary Attack")
        print("Usage: python password_cracker.py <target_hash> <wordlist_file>")
        print("Example: python password_cracker.py 482c811da5d5b4bc6d497ffa98491e38 common_passwords.txt")
        sys.exit(1)
    
    target_hash = sys.argv[1]
    wordlist_file = sys.argv[2]
    
    # Validate hash format (32 characters, hexadecimal)
    if len(target_hash) != 32:
        print("Error: MD5 hash must be exactly 32 characters")
        sys.exit(1)
    
    # Attempt to crack the hash
    print("Password Cracker v1.0")
    print(f"Target: {target_hash}")
    print(f"Wordlist: {wordlist_file}")
    print("-" * 50)
    
    import time
    start_time = time.time()
    
    success, password, attempts = crack_single_hash(target_hash, wordlist_file)
    
    end_time = time.time()
    duration = end_time - start_time
    
    if success:
        print(f"\nSUCCESS!")
        print(f"Password: {password}")
        print(f"Attempts: {attempts}")
        print(f"Duration: {duration:.3f} seconds")
        print(f"Speed: {attempts/duration:.0f} attempts/second")
    else:
        print(f"\nFAILED - Password not found in wordlist")
        print(f"Attempts: {attempts}")
        print(f"Duration: {duration:.3f} seconds")

# Update the main guard
if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Run tests if no arguments provided
        create_test_hashes()
        save_target_hashes()
        create_wordlist()
        print("\n" + "="*60)
        test_crack_known_hash()
        print("\n" + "="*60)
        crack_all_targets()
        print("\n" + "="*60)
        timed_crack_test()
    else:
        # Run as command line tool
        main()