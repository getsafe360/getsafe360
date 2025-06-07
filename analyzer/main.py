# analyzer/main.py
import argparse
import json
from seo import SEOAnalyzer

def main():
    parser = argparse.ArgumentParser(description="GetSafe AI-Agent Optimization Suite")
    parser.add_argument('url', help='The URL of the website to analyze')
    parser.add_argument('--agent', choices=['seo'], default='seo', help='Which agent to run (default: seo)')
    parser.add_argument('--output', choices=['json', 'console'], default='console', help='Output format')
    args = parser.parse_args()

    if args.agent == 'seo':
        analyzer = SEOAnalyzer(args.url)
        result = analyzer.run_all_checks()
    else:
        result = {"error": "Unknown agent selected."}

    if args.output == 'json':
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        # Pretty-print to console for now
        for key, value in result.items():
            print(f"\n{key.upper()}:")
            if isinstance(value, dict):
                for sub_key, sub_val in value.items():
                    print(f"  {sub_key}: {sub_val}")
            else:
                print(f"  {value}")

if __name__ == "__main__":
    main()

import argparse
import json
from seo import SEOAnalyzer

def main():
    parser = argparse.ArgumentParser(description="GetSafe AI-Agent Optimization Suite")
    parser.add_argument('url', help='The URL of the website to analyze')
    parser.add_argument('--agent', choices=['seo'], default='seo', help='Which agent to run (default: seo)')
    parser.add_argument('--output', choices=['json', 'console'], default='console', help='Output format')
    args = parser.parse_args()

    if args.agent == 'seo':
        analyzer = SEOAnalyzer(args.url)
        result = analyzer.run_all_checks()
    else:
        result = {"error": "Unknown agent selected."}

    if args.output == 'json':
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        # Pretty-print to console for now
        for key, value in result.items():
            print(f"\n{key.upper()}:")
            if isinstance(value, dict):
                for sub_key, sub_val in value.items():
                    print(f"  {sub_key}: {sub_val}")
            else:
                print(f"  {value}")

if __name__ == "__main__":
    main()
