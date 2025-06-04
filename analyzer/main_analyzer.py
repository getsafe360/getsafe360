# analyzer/main_analyzer.py

from analyzer.modules.performance import analyze_performance
from analyzer.modules.security import analyze_security
# Future modules:
# from analyzer.modules.seo import analyze_seo
# from analyzer.modules.accessibility import analyze_accessibility

def run_full_analysis(url: str) -> dict:
    """
    Coordinates all module-level analysis functions for a given URL.
    """
    print(f"\n🚀 Starting full analysis for: {url}")

    results = {
        "url": url,
        "performance": analyze_performance(url),
        "security": analyze_security(url),
        # "seo": analyze_seo(url),
        # "accessibility": analyze_accessibility(url),
        "summary": {
            "recommendations_total": 0,
            "critical_issues": 0,
        }
    }

    # 🔍 Tally all recommendations (simple MVP logic)
    all_recs = results["performance"].get("recommendations", []) + \
               results["security"].get("recommendations", [])
    
    results["summary"]["recommendations_total"] = len(all_recs)
    results["summary"]["critical_issues"] = sum(1 for r in all_recs if "!" in r)

    return results

