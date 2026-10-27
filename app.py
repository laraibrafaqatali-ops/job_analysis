import json
from graph import run_analysis


def print_report(r: dict):
    print("\n" + "=" * 40)
    print("      STRUCTURED HIRING REPORT")
    print("=" * 40)
    print(f"Job Title:        {r['job_title']}")
    print(f"Company:          {r['company']}")
    print(f"Experience:       {r['experience']}")
    print(f"Required Skills:  {', '.join(r['required_skills'])}")
    print(f"Job Category:     {r['job_category']}")
    print(f"Employment Type:  {r['employment_type']}")
    print(f"Technical Skills: {', '.join(r['technical_skills'])}")
    print(f"Soft Skills:      {', '.join(r['soft_skills'])}")
    print("Top 3 Skills:")
    for i, skill in enumerate(r["top_3_skills"], 1):
        print(f"  {i}. {skill}")
    print("=" * 40)


def main():
    print("Job Description paste karein (khatam karne ke liye ek khali line + Enter):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            if lines:        # pehle text aa chuka hai, ab khatam
                break
            continue         # shuru ki khali lines ignore karo
        lines.append(line)
    text = "\n".join(lines)

    result = run_analysis(text)
    if "error" in result:
        print(f"\nError: {result['error']}")
        return

    print_report(result["report"])

    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(result["report"], f, indent=2, ensure_ascii=False)
    print("Report report.json mein save ho gayi.")



if __name__ == "__main__":
    main()