#!/usr/bin/env python3
"""
Fix duplicate {% block extra_css %} in templates
"""

import re
import os

templates_dir = "templates"

# Templates that need fixing
templates_to_fix = [
    "5_Teamates.html",
    "6_Domain_Result.html",
    "7_Problem_Statement.html",
    "9_Out_Database.html",
    "imageUpload.html",
]

def fix_template(filepath):
    """Remove duplicate block extra_css declarations"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all {% block extra_css %} ... {% endblock %} sections
    pattern = r'{%\s*block\s+extra_css\s*%}.*?{%\s*endblock\s*%}'
    matches = list(re.finditer(pattern, content, re.DOTALL))
    
    if len(matches) <= 1:
        print(f"✅ {os.path.basename(filepath)} - No duplicates found")
        return False
    
    print(f"⚠️  {os.path.basename(filepath)} - Found {len(matches)} blocks, merging...")
    
    # Extract all CSS content
    all_css = []
    for match in matches:
        block_content = match.group(0)
        # Extract just the CSS between <style> tags
        css_match = re.search(r'<style>(.*?)</style>', block_content, re.DOTALL)
        if css_match:
            all_css.append(css_match.group(1).strip())
    
    # Create merged block
    merged_css = '\n\n'.join(all_css)
    merged_block = f"{{% block extra_css %}}\n<style>\n{merged_css}\n</style>\n{{% endblock %}}"
    
    # Remove all old blocks
    for match in reversed(matches):
        content = content[:match.start()] + content[match.end():]
    
    # Find where to insert the merged block (after {% block title %} if it exists)
    title_match = re.search(r'{%\s*block\s+title\s*%}.*?{%\s*endblock\s*%}', content)
    if title_match:
        insert_pos = title_match.end()
        content = content[:insert_pos] + "\n\n" + merged_block + content[insert_pos:]
    else:
        # Insert after {% extends %}
        extends_match = re.search(r'{%\s*extends.*?%}', content)
        if extends_match:
            insert_pos = extends_match.end()
            content = content[:insert_pos] + "\n\n" + merged_block + content[insert_pos:]
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {os.path.basename(filepath)} - Fixed!")
    return True

def main():
    print("🔧 Fixing duplicate block extra_css in templates...\n")
    
    fixed_count = 0
    for template in templates_to_fix:
        filepath = os.path.join(templates_dir, template)
        if os.path.exists(filepath):
            if fix_template(filepath):
                fixed_count += 1
        else:
            print(f"❌ {template} - File not found")
    
    print(f"\n✅ Fixed {fixed_count} templates")
    print("🎉 Done! Restart the server to see changes.")

if __name__ == "__main__":
    main()
