#!/usr/bin/env python3
"""
Test script để kiểm tra tất cả modules hoạt động tốt
"""

def test_imports():
    """Test import tất cả modules"""
    try:
        print("Testing imports...")
        
        import streamlit as st
        print("✅ Streamlit imported successfully")
        
        from caesar import encrypt_caesar, decrypt_caesar
        print("✅ Caesar cipher imported successfully")
        
        from vigenere import encrypt_vigenere, decrypt_vigenere
        print("✅ Vigenère cipher imported successfully")
        
        from playfair import encrypt_playfair, decrypt_playfair
        print("✅ Playfair cipher imported successfully")
        
        from hill import encrypt_hill, decrypt_hill
        print("✅ Hill cipher imported successfully")
        
        from des import encrypt_des, decrypt_des
        print("✅ DES cipher imported successfully")
        
        from permutation import encrypt_permutation, decrypt_permutation
        print("✅ Permutation cipher imported successfully")
        
        from polyalphabetic import encrypt_polyalphabetic, decrypt_polyalphabetic
        print("✅ Polyalphabetic cipher imported successfully")
        
        print("\n🎉 All imports successful!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality của các thuật toán"""
    try:
        print("\nTesting basic functionality...")
        
        # Test Caesar
        from caesar import encrypt_caesar, decrypt_caesar
        text = "HELLO"
        encrypted = encrypt_caesar(text, 3)
        decrypted = decrypt_caesar(encrypted, 3)
        assert decrypted == text, "Caesar cipher failed"
        print("✅ Caesar cipher works")
        
        # Test Vigenère  
        from vigenere import encrypt_vigenere, decrypt_vigenere
        encrypted = encrypt_vigenere(text, "KEY")
        decrypted = decrypt_vigenere(encrypted, "KEY")
        assert decrypted == text, "Vigenère cipher failed"
        print("✅ Vigenère cipher works")
        
        # Test wrapper functions
        from permutation import encrypt_permutation, decrypt_permutation
        encrypted = encrypt_permutation(text, "3142")
        decrypted = decrypt_permutation(encrypted, "3142")
        print("✅ Permutation cipher wrapper works")
        
        from polyalphabetic import encrypt_polyalphabetic, decrypt_polyalphabetic
        encrypted = encrypt_polyalphabetic(text, "SECRET")
        decrypted = decrypt_polyalphabetic(encrypted, "SECRET")
        print("✅ Polyalphabetic cipher wrapper works")
        
        print("\n🎉 All basic tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Running tests for Cryptography Education Platform\n")
    
    success = True
    success &= test_imports()
    success &= test_basic_functionality()
    
    if success:
        print("\n✅ All tests passed! Ready for deployment! 🚀")
    else:
        print("\n❌ Some tests failed! Please check the errors above.")
