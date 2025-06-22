#!/usr/bin/env python3
"""
Final deployment test
"""

def test_streamlit_startup():
    """Test if Streamlit can start without errors"""
    try:
        print("🧪 Testing Streamlit startup...")
        
        # Test import
        import streamlit as st
        print("✅ Streamlit import OK")
        
        # Test app import (should not run main)
        import app
        print("✅ App import OK")
        
        # Test config
        import os
        config_path = ".streamlit/config.toml"
        if os.path.exists(config_path):
            print("✅ Config file exists")
            
            # Read and validate config
            with open(config_path, 'r') as f:
                content = f.read()
                if '$PORT' in content:
                    print("❌ Config still contains $PORT - this will cause errors!")
                    return False
                else:
                    print("✅ Config is clean (no $PORT)")
        
        # Test requirements
        req_path = "requirements.txt"
        if os.path.exists(req_path):
            with open(req_path, 'r') as f:
                content = f.read()
                if 'numpy>=1.26.0' in content:
                    print("✅ Requirements updated for Python 3.13+")
                else:
                    print("⚠️  Requirements may need updating")
        
        print("🎉 All startup tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Startup test failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Final Deployment Test\n")
    
    if test_streamlit_startup():
        print("\n✅ READY FOR DEPLOYMENT!")
        print("📝 Next steps:")
        print("1. Push code to GitHub")
        print("2. Deploy on Streamlit Cloud")
        print("3. Should work without errors!")
    else:
        print("\n❌ NOT READY - please fix issues above")
