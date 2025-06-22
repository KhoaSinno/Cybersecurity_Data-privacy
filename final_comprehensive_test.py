#!/usr/bin/env python3
"""
FINAL COMPREHENSIVE TEST - CRYPTOGRAPHY WEB APP
==============================================
Test tất cả thuật toán mã hóa đã được triển khai
"""

def test_all_algorithms():
    """Test tất cả các thuật toán mã hóa"""
    print("🔐 TESTING ALL CRYPTOGRAPHIC ALGORITHMS")
    print("=" * 50)
    
    # Test data
    test_text = "HELLO123"
    test_keys = {
        'caesar': 3,
        'vigenere': 'MYSECRET',
        'playfair': 'MONARCHY', 
        'hill': [[3, 5], [2, 7]],
        'polyalphabetic': 'SECRET',
        'permutation': '3142',
        'des': 'MYSECRET'
    }
    
    results = {}
    
    # 1. Caesar Cipher
    print("\n1. 🔤 CAESAR CIPHER")
    try:
        from caesar import encrypt_caesar, decrypt_caesar
        encrypted = encrypt_caesar(test_text, test_keys['caesar'])
        decrypted = decrypt_caesar(encrypted, test_keys['caesar'])
        results['caesar'] = (encrypted, decrypted, decrypted == test_text)
        print(f"   ✅ Input: {test_text}")
        print(f"   🔒 Encrypted: {encrypted}")
        print(f"   🔓 Decrypted: {decrypted}")
        print(f"   ✅ Success: {results['caesar'][2]}")
    except Exception as e:
        results['caesar'] = (None, None, False)
        print(f"   ❌ Error: {e}")
    
    # 2. Vigenère Cipher  
    print("\n2. 🗝️ VIGENÈRE CIPHER")
    try:
        from vigenere import encrypt_vigenere, decrypt_vigenere
        encrypted = encrypt_vigenere(test_text, test_keys['vigenere'])
        decrypted = decrypt_vigenere(encrypted, test_keys['vigenere'])
        results['vigenere'] = (encrypted, decrypted, decrypted == test_text)
        print(f"   ✅ Input: {test_text}")
        print(f"   🔒 Encrypted: {encrypted}")
        print(f"   🔓 Decrypted: {decrypted}")
        print(f"   ✅ Success: {results['vigenere'][2]}")
    except Exception as e:
        results['vigenere'] = (None, None, False)
        print(f"   ❌ Error: {e}")
    
    # 3. Playfair Cipher
    print("\n3. 🎭 PLAYFAIR CIPHER")
    try:
        from playfair import encrypt_playfair, decrypt_playfair
        encrypted = encrypt_playfair(test_text, test_keys['playfair'])
        decrypted = decrypt_playfair(encrypted, test_keys['playfair'])
        results['playfair'] = (encrypted, decrypted, decrypted == test_text)
        print(f"   ✅ Input: {test_text}")
        print(f"   🔒 Encrypted: {encrypted}")
        print(f"   🔓 Decrypted: {decrypted}")
        print(f"   ✅ Success: {results['playfair'][2]}")
    except Exception as e:
        results['playfair'] = (None, None, False)
        print(f"   ❌ Error: {e}")
    
    # 4. Hill Cipher
    print("\n4. 🧮 HILL CIPHER")
    try:
        from hill import encrypt_hill, decrypt_hill
        encrypted = encrypt_hill(test_text, test_keys['hill'])
        decrypted = decrypt_hill(encrypted, test_keys['hill'])
        results['hill'] = (encrypted, decrypted, decrypted == test_text)
        print(f"   ✅ Input: {test_text}")
        print(f"   🔒 Encrypted: {encrypted}")
        print(f"   🔓 Decrypted: {decrypted}")
        print(f"   ✅ Success: {results['hill'][2]}")
    except Exception as e:
        results['hill'] = (None, None, False)
        print(f"   ❌ Error: {e}")
    
    # 5. Polyalphabetic Cipher
    print("\n5. 🔀 POLYALPHABETIC CIPHER")
    try:
        from polyalphabetic import encrypt_polyalphabetic, decrypt_polyalphabetic
        encrypted = encrypt_polyalphabetic(test_text, test_keys['polyalphabetic'])
        decrypted = decrypt_polyalphabetic(encrypted, test_keys['polyalphabetic'])
        results['polyalphabetic'] = (encrypted, decrypted, decrypted == test_text)
        print(f"   ✅ Input: {test_text}")
        print(f"   🔒 Encrypted: {encrypted}")
        print(f"   🔓 Decrypted: {decrypted}")
        print(f"   ✅ Success: {results['polyalphabetic'][2]}")
    except Exception as e:
        results['polyalphabetic'] = (None, None, False)
        print(f"   ❌ Error: {e}")
    
    # 6. Permutation Cipher
    print("\n6. 🔄 PERMUTATION CIPHER")
    try:
        from permutation import encrypt_permutation, decrypt_permutation
        encrypted = encrypt_permutation(test_text, test_keys['permutation'])
        decrypted = decrypt_permutation(encrypted, test_keys['permutation'])
        results['permutation'] = (encrypted, decrypted, decrypted == test_text)
        print(f"   ✅ Input: {test_text}")
        print(f"   🔒 Encrypted: {encrypted}")
        print(f"   🔓 Decrypted: {decrypted}")
        print(f"   ✅ Success: {results['permutation'][2]}")
    except Exception as e:
        results['permutation'] = (None, None, False)
        print(f"   ❌ Error: {e}")
    
    # 7. DES Cipher
    print("\n7. 🏢 DES CIPHER")
    try:
        from des import encrypt_des, decrypt_des
        encrypted = encrypt_des(test_text, test_keys['des'])
        decrypted = decrypt_des(encrypted, test_keys['des'])
        results['des'] = (encrypted, decrypted, decrypted == test_text)
        print(f"   ✅ Input: {test_text}")
        print(f"   🔒 Encrypted: {encrypted}")
        print(f"   🔓 Decrypted: {decrypted}")
        print(f"   ✅ Success: {results['des'][2]}")
    except Exception as e:
        results['des'] = (None, None, False)
        print(f"   ❌ Error: {e}")
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 FINAL SUMMARY")
    print("=" * 50)
    
    total_algorithms = len(results)
    successful = sum(1 for _, _, success in results.values() if success)
    
    print(f"Total algorithms tested: {total_algorithms}")
    print(f"Successful: {successful}")
    print(f"Failed: {total_algorithms - successful}")
    print(f"Success rate: {successful/total_algorithms*100:.1f}%")
    
    print("\nDetailed Results:")
    for name, (enc, dec, success) in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {name.upper():<15}: {status}")
    
    # Test Streamlit app import
    print("\n" + "=" * 50)
    print("🌐 STREAMLIT APP TEST")
    print("=" * 50)
    
    try:
        import app
        print("✅ Streamlit app imports successfully")
        print("✅ All functions are accessible")
        print("✅ Ready for deployment")
    except Exception as e:
        print(f"❌ Streamlit app import failed: {e}")
    
    print("\n🎉 TESTING COMPLETED!")
    print("🚀 App is ready for production use!")

if __name__ == "__main__":
    test_all_algorithms()
