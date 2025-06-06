# analyzer/modules/performance.py
# test or orchestrator
from analyzer.modules.performance import analyze_performance

url = "https://example.com"
report = analyze_performance(url)
print(report)

# analyzer/modules/security.py
from analyzer.modules.security import analyze_security

url = "https://example.com"
security_report = analyze_security(url)
print(security_report)

# analyzer/main_analyzer.py
from analyzer.main_analyzer import run_full_analysis

if __name__ == "__main__":
    url = input("Enter the website URL to analyze: ")
    final_report = run_full_analysis(url)
    
    print("\n✅ Full Report:")
    print(final_report)

    
# If you want to test quickly:
if __name__ == "__main__":
    url = "https://example.com"
    analyzer = SEOAnalyzer(url)
    results = analyzer.run_all_checks()
    import json
    print(json.dumps(results, indent=2, ensure_ascii=False))

