from groq import Groq
from platforms import PLATFORMS, TONES, VARIATION_ANGLES
import json
import re
import os
from datetime import datetime

API_KEY = "Paste your API key here"
client = Groq(api_key=API_KEY)

# ── MAIN GENERATION FUNCTION ──────────────────────────────────────────
def generate_ad_copies(product, description, audience, platforms, tone, variations_count):
    """
    Generates platform-specific ad copies with A/B variations
    and performance analysis for each variation — all in one API call.
    """
    results = {}

    for platform_key in platforms:
        if platform_key not in PLATFORMS:
            continue

        platform = PLATFORMS[platform_key]
        tone_desc = TONES.get(tone, TONES["professional"])
        angles = VARIATION_ANGLES[:variations_count]

        prompt = build_generation_prompt(
            product, description, audience,
            platform, tone_desc, angles
        )

        print(f"Generating copies for {platform['name']}...")

        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": get_system_prompt()},
                    {"role": "user",   "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.8
            )

            raw = response.choices[0].message.content
            print(f"Raw response for {platform['name']}:", raw[:200])

            parsed = extract_json(raw)
            if parsed:
                results[platform_key] = {
                    "platform_name": platform["name"],
                    "platform_icon": platform["icon"],
                    "platform_color": platform["color"],
                    "variations": parsed.get("variations", [])
                }
            else:
                results[platform_key] = {
                    "platform_name": platform["name"],
                    "error": "Could not parse AI response"
                }

        except Exception as e:
            print(f"Error generating for {platform['name']}: {e}")
            results[platform_key] = {
                "platform_name": platform["name"],
                "error": str(e)
            }

    save_to_history(product, audience, tone, platforms, results)
    return results


# ── SYSTEM PROMPT ─────────────────────────────────────────────────────
def get_system_prompt():
    return """You are an expert digital marketing copywriter with 10+ years of experience 
creating high-converting ad copies for global brands across all major platforms.
You understand platform-specific best practices, psychological triggers, and conversion 
optimization principles. You always respond with ONLY valid JSON — no explanation, 
no markdown, no preamble. Just the raw JSON object."""


# ── GENERATION PROMPT ─────────────────────────────────────────────────
def build_generation_prompt(product, description, audience, platform, tone_desc, angles):
    angles_text = "\n".join([
        f"- Variation {a['id']} ({a['label']}): {a['desc']}"
        for a in angles
    ])

    return f"""Generate {len(angles)} A/B test ad copy variations for this campaign:

PRODUCT/SERVICE: {product}
KEY BENEFITS/DESCRIPTION: {description}
TARGET AUDIENCE: {audience}
PLATFORM: {platform['name']}
TONE: {tone_desc}
PLATFORM RULES: {platform['rules']}

VARIATION ANGLES TO USE:
{angles_text}

For each variation, also analyze its performance and provide scores + suggestions.

Return ONLY this exact JSON (no other text):
{{
  "variations": [
    {{
      "id": "A",
      "label": "Feature-Focused",
      "headline": "your headline here",
      "subheadline": "optional subheadline or second headline",
      "body": "your main ad copy body text here",
      "cta": "Call To Action Text",
      "hashtags": "#tag1 #tag2",
      "scores": {{
        "headline_strength": 85,
        "emotional_appeal": 72,
        "clarity": 90,
        "cta_effectiveness": 78,
        "overall": 81
      }},
      "strengths": ["strength 1", "strength 2"],
      "suggestions": ["suggestion 1", "suggestion 2"]
    }}
  ]
}}

Make the copies genuinely compelling, platform-appropriate, and conversion-optimized.
Scores should be honest (not all 90+). Suggestions must be specific and actionable."""


# ── JSON EXTRACTION WITH FALLBACKS ────────────────────────────────────
def extract_json(text):
    # Method 1: Direct parse
    try:
        return json.loads(text.strip())
    except:
        pass

    # Method 2: Extract from ```json blocks
    try:
        match = re.search(r'```json\s*(.*?)\s*```', text, re.DOTALL)
        if match:
            return json.loads(match.group(1).strip())
    except:
        pass

    # Method 3: Extract from ``` blocks
    try:
        match = re.search(r'```\s*(.*?)\s*```', text, re.DOTALL)
        if match:
            return json.loads(match.group(1).strip())
    except:
        pass

    # Method 4: Find JSON object
    try:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            return json.loads(match.group(0))
    except:
        pass

    return None


# ── SAVE TO HISTORY ───────────────────────────────────────────────────
def save_to_history(product, audience, tone, platforms, results):
    history_file = "history.json"
    history = []

    if os.path.exists(history_file):
        try:
            with open(history_file, "r") as f:
                history = json.load(f)
        except:
            history = []

    entry = {
        "id": len(history) + 1,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "product": product,
        "audience": audience,
        "tone": tone,
        "platforms": platforms,
        "results": results
    }

    history.append(entry)

    with open(history_file, "w") as f:
        json.dump(history, f, indent=2)

    print(f"Saved to history: {product}")


# ── EXPORT HELPERS ────────────────────────────────────────────────────
def results_to_csv(product, results):
    """Convert results to CSV format for Google Sheets."""
    lines = ["Platform,Variation,Label,Headline,Body,CTA,Hashtags,Overall Score,Suggestions"]

    for platform_key, data in results.items():
        if "error" in data:
            continue
        for v in data.get("variations", []):
            headline  = v.get("headline", "").replace(",", ";")
            body      = v.get("body", "").replace(",", ";")
            cta       = v.get("cta", "").replace(",", ";")
            hashtags  = v.get("hashtags", "").replace(",", ";")
            score     = v.get("scores", {}).get("overall", 0)
            sugg      = " | ".join(v.get("suggestions", [])).replace(",", ";")

            lines.append(
                f'{data["platform_name"]},{v["id"]},{v["label"]},'
                f'"{headline}","{body}","{cta}","{hashtags}",{score},"{sugg}"'
            )

    return "\n".join(lines)


def results_to_notion(product, audience, tone, results):
    """Convert results to Notion-friendly Markdown."""
    md = [f"# 📣 Ad Campaign: {product}", f"", f"**Target Audience:** {audience}  ",
          f"**Tone:** {tone.title()}  ", f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]

    for platform_key, data in results.items():
        if "error" in data:
            continue
        md.append(f"---")
        md.append(f"## {data['platform_icon']} {data['platform_name']}")
        md.append("")

        for v in data.get("variations", []):
            score = v.get("scores", {}).get("overall", 0)
            md.append(f"### Variation {v['id']} — {v['label']} (Score: {score}/100)")
            md.append(f"")
            md.append(f"**Headline:** {v.get('headline', '')}")
            if v.get("subheadline"):
                md.append(f"**Subheadline:** {v.get('subheadline', '')}")
            md.append(f"")
            md.append(f"**Body Copy:**")
            md.append(f"> {v.get('body', '')}")
            md.append(f"")
            md.append(f"**CTA:** {v.get('cta', '')}")
            if v.get("hashtags"):
                md.append(f"**Hashtags:** {v.get('hashtags', '')}")
            md.append(f"")
            if v.get("strengths"):
                md.append(f"✅ **Strengths:** {' · '.join(v['strengths'])}")
            if v.get("suggestions"):
                md.append(f"💡 **Suggestions:** {' · '.join(v['suggestions'])}")
            md.append("")

    return "\n".join(md)