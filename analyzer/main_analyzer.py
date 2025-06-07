from analyzer.modules.performance import analyze_performance
from analyzer.modules.security import analyze_security
from analyzer.modules.seo import SEOAnalyzer
from analyzer.modules.serp import SERPAnalyzer
# from analyzer.modules.accessibility import analyze_accessibility

def run_full_analysis(url: str) -> dict:
    print(f"\n🚀 Starting full analysis for: {url}")
    seo = SEOAnalyzer(url)
    serp = SERPAnalyzer(url)

    results = {
        "url": url,
        "performance": analyze_performance(url) if 'analyze_performance' in globals() else "Not implemented",
        "security": analyze_security(url) if 'analyze_security' in globals() else "Not implemented",
        "seo": seo.run_all_checks(),
        "reputation": serp.run_analysis(),
        # "accessibility": analyze_accessibility(url) if 'analyze_accessibility' in globals() else "Not implemented",
        "summary": {
            "recommendations_total": 0,  # Expand as modules report recommendations
            "critical_issues": 0,
        }
    }
    # Simple tally placeholder (expand for your real needs)
    recommendations = []
    for key in ("performance", "security"):
        mod = results.get(key)
        if isinstance(mod, dict) and "recommendations" in mod:
            recommendations += mod["recommendations"]
    results["summary"]["recommendations_total"] = len(recommendations)
    results["summary"]["critical_issues"] = sum(1 for r in recommendations if "!" in r)

    return results
