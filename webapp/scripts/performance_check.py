"""
Performance Check Script for SkinCare AI Website
Analyzes templates for performance issues and provides recommendations
"""

import os
import re
from pathlib import Path

def check_template_performance(template_path):
    """Check a single template for performance issues"""
    issues = []
    recommendations = []
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for inline styles (should use CSS classes)
    inline_styles = len(re.findall(r'style="[^"]*"', content))
    if inline_styles > 10:
        issues.append(f"⚠️  {inline_styles} inline styles found (consider using CSS classes)")
    
    # Check for animations
    animations = len(re.findall(r'animation:|@keyframes', content))
    if animations > 0:
        issues.append(f"⚠️  {animations} animations found (may impact performance)")
    
    # Check for transforms
    transforms = len(re.findall(r'transform:', content))
    if transforms > 5:
        issues.append(f"⚠️  {transforms} transforms found (use sparingly)")
    
    # Check for backdrop-filter (can be expensive)
    backdrop_filters = len(re.findall(r'backdrop-filter:', content))
    if backdrop_filters > 0:
        recommendations.append(f"ℹ️  {backdrop_filters} backdrop-filter uses (GPU intensive)")
    
    # Check for box-shadow
    box_shadows = len(re.findall(r'box-shadow:', content))
    if box_shadows > 10:
        recommendations.append(f"ℹ️  {box_shadows} box-shadow uses (consider reducing)")
    
    # Check for large images without optimization
    img_tags = len(re.findall(r'<img[^>]*>', content))
    if img_tags > 0:
        recommendations.append(f"ℹ️  {img_tags} images found (ensure they're optimized)")
    
    # Check for external resources
    external_links = len(re.findall(r'https?://', content))
    if external_links > 5:
        recommendations.append(f"ℹ️  {external_links} external resources (may slow initial load)")
    
    return issues, recommendations

def analyze_all_templates():
    """Analyze all templates in the templates directory"""
    templates_dir = Path('templates')
    
    if not templates_dir.exists():
        print("❌ Templates directory not found!")
        return
    
    print("=" * 80)
    print("🔍 PERFORMANCE CHECK - SkinCare AI Website")
    print("=" * 80)
    print()
    
    total_issues = 0
    total_recommendations = 0
    
    for template_file in sorted(templates_dir.glob('*.html')):
        issues, recommendations = check_template_performance(template_file)
        
        if issues or recommendations:
            print(f"📄 {template_file.name}")
            print("-" * 80)
            
            if issues:
                print("  Issues:")
                for issue in issues:
                    print(f"    {issue}")
                total_issues += len(issues)
            
            if recommendations:
                print("  Recommendations:")
                for rec in recommendations:
                    print(f"    {rec}")
                total_recommendations += len(recommendations)
            
            print()
    
    print("=" * 80)
    print(f"📊 SUMMARY")
    print("=" * 80)
    print(f"Total Issues: {total_issues}")
    print(f"Total Recommendations: {total_recommendations}")
    print()
    
    # Performance score
    score = max(0, 100 - (total_issues * 5) - (total_recommendations * 2))
    print(f"⭐ Performance Score: {score}/100")
    
    if score >= 90:
        print("✅ Excellent! Website is well optimized.")
    elif score >= 70:
        print("✅ Good! Minor optimizations recommended.")
    elif score >= 50:
        print("⚠️  Fair. Several optimizations needed.")
    else:
        print("❌ Poor. Significant optimizations required.")
    
    print()
    print("=" * 80)
    print("💡 GENERAL RECOMMENDATIONS")
    print("=" * 80)
    print("1. ✅ Use CSS classes instead of inline styles")
    print("2. ✅ Minimize animations and transforms")
    print("3. ✅ Optimize images (compress, use WebP)")
    print("4. ✅ Lazy load images below the fold")
    print("5. ✅ Use font-display: swap for web fonts")
    print("6. ✅ Minimize external resources")
    print("7. ✅ Use will-change sparingly")
    print("8. ✅ Avoid layout thrashing")
    print("9. ✅ Use CSS containment where possible")
    print("10. ✅ Enable gzip/brotli compression")
    print()

if __name__ == "__main__":
    analyze_all_templates()
