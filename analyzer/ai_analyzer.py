"""
AI Analyzer Entry Point for GetSafe360

This script initializes and coordinates modules that analyze websites for:
- Performance & speed
- Security & compliance
- SEO & AI readiness
- Accessibility (BFSG)
"""

import sys
from modules.performance import check_performance
from modules.security import check_security
from modules.seo import check_seo
from modules.accessibility import check_accessibility

def run_full_analysis(url: str):
    results = {
        "performance": check_performance(url),
        "security": check_security(url),
        "seo": check_seo(url),
        "accessibility": check_accessibility(url)
    }
    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ai_analyzer.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    print(f"\n🔍 Running full analysis for: {url}")
    output = run_full_analysis(url)
    print("\n✅ Analysis Complete:")
    for category, result in output.items():
        print(f"- {category.title()}: {result}")
