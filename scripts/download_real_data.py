"""Download real data for all scientist profiles from public web sources."""

import json, time, requests
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "scientist_taste" / "data" / "profiles"
DATA_DIR.mkdir(parents=True, exist_ok=True)
HEADERS = {"User-Agent": "ScientistResearchTaste/0.1 (academic research)"}

def fetch(url, delay=1.0):
    time.sleep(delay)
    try:
        r = requests.get(url, headers=HEADERS, timeout=30)
        r.raise_for_status()
        return r
    except Exception as e:
        print(f"  FAIL: {e}")
        return None

def download_wikipedia_profiles():
    """Download Wikipedia summaries for all scientists."""
    scientists = {
        # Classical
        "Albert_Einstein": "einstein",
        "Richard_Feynman": "feynman",
        "Isaac_Newton": "newton",
        "Gregor_Mendel": "mendel",
        "Galileo_Galilei": "galileo",
        # Nobel
        "Jennifer_Doudna": "doudna",
        "Geoffrey_Hinton": "hinton",
        "Katalin_Karik%C3%B3": "kariko",
        "Roger_Penrose": "penrose",
        "Shinya_Yamanaka": "yamanaka",
        # PIs
        "Uri_Alon": "uri_alon",
        "Terence_Tao": "terence_tao",
        "Manu_Prakash": "manu_prakash",
        "Carolyn_Bertozzi": "carolyn_bertozzi",
    }

    results = {}
    for page, key in scientists.items():
        r = fetch(f"https://en.wikipedia.org/api/rest_v1/page/summary/{page}")
        if r:
            d = r.json()
            results[key] = {
                "title": d.get("title", ""),
                "extract": d.get("extract", ""),
                "description": d.get("description", ""),
            }
            print(f"  OK: {key} ({len(d.get('extract',''))} chars)")

    # Full extracts for key scientists
    for page in ["Isaac_Newton", "Gregor_Mendel", "Galileo_Galilei", "Jennifer_Doudna", "Geoffrey_Hinton"]:
        key = scientists[page]
        r = fetch(f"https://en.wikipedia.org/w/api.php?action=query&titles={page}&prop=extracts&exintro=false&explaintext=true&format=json")
        if r:
            d = r.json()
            pd = list(d.get("query",{}).get("pages",{}).values())
            if pd:
                text = pd[0].get("extract","")
                results[key]["full_extract"] = text[:20000]
                print(f"  FULL: {key} ({len(text)} chars)")

    (DATA_DIR / "wikipedia_profiles.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    return results

def download_nobel_pages():
    """Download Nobel Prize biography pages."""
    print("\n=== Nobel Prize Pages ===")
    nobel = {
        "doudna_2020": "https://en.wikipedia.org/api/rest_v1/page/summary/Nobel_Prize_in_Chemistry#2020",
        "hinton_2024": "https://en.wikipedia.org/api/rest_v1/page/summary/CRISPR_gene_editing",
        "kariko_mRNA": "https://en.wikipedia.org/api/rest_v1/page/summary/MRNA_vaccine",
        "penrose_singularity": "https://en.wikipedia.org/api/rest_v1/page/summary/Penrose%E2%80%93Hawking_singularity_theorems",
        "yamanaka_ipsc": "https://en.wikipedia.org/api/rest_v1/page/summary/Induced_pluripotent_stem_cell",
        "bertozzi_click": "https://en.wikipedia.org/api/rest_v1/page/summary/Click_chemistry",
        "jumper_alphafold": "https://en.wikipedia.org/api/rest_v1/page/summary/AlphaFold",
    }
    results = {}
    for key, url in nobel.items():
        r = fetch(url)
        if r:
            d = r.json()
            results[key] = {"title": d.get("title",""), "extract": d.get("extract","")}
            print(f"  OK: {key}")

    (DATA_DIR / "nobel_related.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")

def download_wikiquotes():
    """Download quotes for key scientists."""
    print("\n=== Wikiquote Scientists ===")
    scientists = ["Isaac_Newton", "Galileo_Galilei"]
    results = {}
    for name in scientists:
        r = fetch(f"https://en.wikiquote.org/w/api.php?action=query&titles={name}&prop=extracts&explaintext=true&format=json")
        if r:
            d = r.json()
            pd = list(d.get("query",{}).get("pages",{}).values())
            if pd:
                text = pd[0].get("extract","")
                results[name] = text[:30000]
                print(f"  OK: {name} ({len(text)} chars)")

    (DATA_DIR / "wikiquotes.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")

def main():
    print("=" * 60)
    print("DOWNLOADING REAL SCIENTIST PROFILE DATA")
    print("=" * 60)
    print("\n=== Wikipedia Profiles ===")

    download_wikipedia_profiles()
    download_nobel_pages()
    download_wikiquotes()

    print("\n=== Download Summary ===")
    total = 0
    for f in sorted(DATA_DIR.glob("*.json")):
        s = f.stat().st_size
        total += s
        print(f"  {f.name}: {s:,} bytes")
    print(f"  TOTAL: {total:,} bytes ({total/1024:.1f} KB)")

if __name__ == "__main__":
    main()
