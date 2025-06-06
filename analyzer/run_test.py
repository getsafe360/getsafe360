from analyzer.modules.seo import SEOAnalyzer
from analyzer.modules.serp import SERPAnalyzer

def test_analysis(url, brand_or_domain):
    print(f"--- SEO Analysis for: {url} ---")
    seo = SEOAnalyzer(url)
    seo_result = seo.run_all_checks()
    for k, v in seo_result.items():
        print(f"\n{k.upper()}:")
        print(v)

    print(f"\n--- SERP Reputation Analysis for: {brand_or_domain} ---")
    serp = SERPAnalyzer(brand_or_domain)
    serp_result = serp.run_analysis()
    print(f"Overall Sentiment: {serp_result['sentiment']}")
    print("Top results:")
    for res in serp_result['results'][:3]:
        print(f"- {res['title']}\n  {res['snippet']}\n")

    # Combine both for a unified JSON report if needed
    return {
        "onpage": seo_result,
        "reputation": serp_result
    }

if __name__ == "__main__":
    # Example usage: run both modules for malkodent.com
    url = "https://malkodent.com/"
    brand_or_domain = "malkodent"
    test_analysis(url, brand_or_domain)
