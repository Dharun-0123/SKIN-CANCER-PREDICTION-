#!/usr/bin/env python3
"""
Debug script to check video background implementation
"""

import os

def debug_video_background():
    print("🔍 Debugging Video Background Implementation")
    print("=" * 50)
    
    # Check if video file exists
    video_path = "webapp/static/images/frontvideo.mp4"
    if os.path.exists(video_path):
        size_mb = os.path.getsize(video_path) / (1024 * 1024)
        print(f"✅ Video file exists: {video_path} ({size_mb:.1f} MB)")
    else:
        print(f"❌ Video file missing: {video_path}")
        return
    
    # Check landing page template
    template_path = "webapp/templates/1_Landing.html"
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        print(f"✅ Landing template exists: {template_path}")
        
        # Check for video background elements
        if 'video-background' in content:
            print("✅ Video background div found")
        else:
            print("❌ Video background div NOT found")
            
        if 'frontvideo.mp4' in content:
            print("✅ frontvideo.mp4 referenced in template")
        else:
            print("❌ frontvideo.mp4 NOT referenced in template")
            
        if 'floating-video-background.css' in content:
            print("✅ CSS file linked")
        else:
            print("❌ CSS file NOT linked")
            
        if 'floating-video-background.js' in content:
            print("✅ JavaScript file linked")
        else:
            print("❌ JavaScript file NOT linked")
            
        # Check body background
        if 'background: transparent' in content:
            print("✅ Body background set to transparent")
        else:
            print("❌ Body background NOT set to transparent")
    
    # Check CSS file
    css_path = "webapp/static/css/floating-video-background.css"
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
            
        print(f"✅ CSS file exists: {css_path}")
        
        # Check opacity values
        if 'opacity: 0.6' in css_content:
            print("✅ Main video opacity set to 0.6 (visible)")
        else:
            print("❌ Main video opacity NOT set to visible level")
            
        # Check z-index
        if 'z-index: -2' in css_content:
            print("✅ Video z-index set to -2 (behind content)")
        else:
            print("❌ Video z-index NOT properly set")
    
    print("\n🎯 Debugging Tips:")
    print("1. Open browser developer tools (F12)")
    print("2. Check Console tab for JavaScript errors")
    print("3. Check Network tab to see if video loads")
    print("4. Check Elements tab to see if video element exists")
    print("5. Try temporarily setting video opacity to 1.0 for testing")
    
    print("\n🔧 Quick Fix CSS (for testing):")
    print(".video-background video { opacity: 1.0 !important; }")

if __name__ == "__main__":
    debug_video_background()