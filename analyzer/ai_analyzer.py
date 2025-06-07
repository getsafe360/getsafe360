"""
AI Analyzer Entry Point for GetSafe360

This script initializes and coordinates modules that analyze websites for:
- Performance & speed
- Security & compliance
- SEO & AI readiness
- Reputation & sentiment (SERP)
- Accessibility (BFSG)
"""

import sys
from analyzer.modules.performance import analyze_performance
from analyzer.modules.security import analyze_security
from analyzer.modules.seo import SEOAnalyzer
from analyzer.modules.serp import SERPAnalyzer
# from analyzer.modules.accessibility import analyze_accessibility   # (if implemented)

def run_full_analysis(url: str) -> dict:
    seo = SEOAnalyzer(url)
    serp = SERPAnalyzer(url)   # or SERPAnalyzer(brand/domain name)

    results = {
        "performance": analyze_performance(url) if 'analyze_performance' in globals() else "Not implemented",
        "security": analyze_security(url) if 'analyze_security' in globals() else "Not implemented",
        "seo": seo.run_all_checks(),
        "reputation": serp.run_analysis(),
        # "accessibility": analyze_accessibility(url) if 'analyze_accessibility' in globals() else "Not implemented"
    }
    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m analyzer.ai_analyzer <URL>")
        sys.exit(1)

    url = sys.argv[1]
    print(f"\n🔍 Running full analysis for: {url}")
    output = run_full_analysis(url)
    print("\n✅ Analysis Complete:")
    for category, result in output.items():
        print(f"\n--- {category.title()} ---")
        print(result)
