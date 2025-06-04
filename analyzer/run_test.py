# run_test.py

from analyzer.modules.seo import SEOAnalyzer

def test_seo_analysis(url):
    analyzer = SEOAnalyzer(url)
    results = analyzer.run_all_checks()
    print("\n=== SEO Analysis Results ===")
    for key, value in results.items():
        print(f"\n{key.capitalize()}:")
        for subkey, subval in value.items():
            print(f"  {subkey}: {subval}")

if __name__ == "__main__":
    test_url = "https://malkodent.com/"
    test_seo_analysis(test_url)

