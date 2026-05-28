# Platform-specific rules, character limits, and best practices
PLATFORMS = {
    "google": {
        "name": "Google Ads",
        "icon": "🔍",
        "color": "#4285f4",
        "headline_limit": 30,
        "description_limit": 90,
        "format": "Search Ad",
        "rules": "Max 3 headlines (30 chars each), 2 descriptions (90 chars each). Include keywords. Sentence case. No exclamation in headline.",
        "tips": ["Include target keywords in headline", "Use numbers for credibility", "Add clear CTA in description"]
    },
    "facebook": {
        "name": "Facebook",
        "icon": "📘",
        "color": "#1877f2",
        "primary_limit": 125,
        "headline_limit": 40,
        "description_limit": 30,
        "format": "Feed Ad",
        "rules": "Primary text: 125 chars recommended. Headline: 40 chars max. Description: 30 chars. Lead with the hook in the first line.",
        "tips": ["Lead with value proposition", "Use social proof when possible", "Keep primary text under 3 lines to avoid truncation"]
    },
    "instagram": {
        "name": "Instagram",
        "icon": "📸",
        "color": "#e1306c",
        "caption_limit": 2200,
        "recommended_limit": 125,
        "hashtag_count": 5,
        "format": "Feed / Story Ad",
        "rules": "Caption recommended under 125 chars (first 2 lines visible). Include 3-5 relevant hashtags. Visual and lifestyle-focused tone.",
        "tips": ["Hook in first 125 characters", "Lifestyle and emotion-focused", "Include 3-5 targeted hashtags"]
    },
    "linkedin": {
        "name": "LinkedIn",
        "icon": "💼",
        "color": "#0a66c2",
        "intro_limit": 150,
        "headline_limit": 70,
        "format": "Sponsored Content",
        "rules": "Introductory text: 150 chars. Headline: 70 chars max. Professional tone. B2B focus. Lead with insight or statistic.",
        "tips": ["Start with a compelling insight or stat", "Professional and authoritative tone", "Focus on business value and ROI"]
    },
    "twitter": {
        "name": "Twitter / X",
        "icon": "🐦",
        "color": "#1da1f2",
        "tweet_limit": 280,
        "format": "Promoted Tweet",
        "rules": "Max 280 characters total including spaces. Concise and punchy. 1-2 hashtags max. Include a link or CTA. Conversational tone.",
        "tips": ["Use power words in the first 5 words", "Keep hashtags to 1-2 maximum", "Conversational and direct voice"]
    }
}

TONES = {
    "professional":  "authoritative, polished, business-focused, and credibility-building",
    "casual":        "friendly, conversational, warm, and approachable — like talking to a friend",
    "urgent":        "time-sensitive, action-driving, with FOMO and scarcity elements",
    "humorous":      "witty, playful, clever, and memorable — uses light humor and wordplay",
    "emotional":     "empathetic, inspiring, feeling-focused, and story-driven",
    "minimalist":    "ultra-clean, direct, stripped of fluff — maximum impact in fewest words"
}

VARIATION_ANGLES = [
    {"id": "A", "label": "Feature-Focused",  "desc": "Highlight what the product IS and does — specs, features, capabilities"},
    {"id": "B", "label": "Benefit-Focused",  "desc": "Highlight how it IMPROVES the customer's life, solves their pain point"},
    {"id": "C", "label": "Urgency-Focused",  "desc": "Create FOMO, time-sensitivity, scarcity, or exclusive offer framing"}
]