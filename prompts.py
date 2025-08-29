"""
Prompt templates for each function. We provide 3 distinct prompt variants per function,
varying in tone, specificity, and structure.
"""

from dataclasses import dataclass
from typing import List, Dict
import random

@dataclass
class PromptVariant:
    name: str
    system: str
    user_template: str

def choose_variant(variants: List[PromptVariant]) -> PromptVariant:
    return random.choice(variants)

# 1) Answer Questions
ANSWER_QUESTION_VARIANTS: List[PromptVariant] = [
    PromptVariant(
        name="concise_factual",
        system="You are a concise, accurate assistant. If unsure, say so briefly.",
        user_template="Answer factually and briefly: {question}"
    ),
    PromptVariant(
        name="teacherly_explain",
        system="You are a friendly teacher. Explain clearly and avoid jargon unless needed.",
        user_template="Please answer this question and add a short explanation: {question}"
    ),
    PromptVariant(
        name="contextual_bullets",
        system="You respond with a short answer followed by 3 bullet-point facts.",
        user_template="Question: {question}\nProvide a 1-sentence answer, then 3 bullets with key context."
    ),
]

# 2) Summarize Text
SUMMARIZE_TEXT_VARIANTS: List[PromptVariant] = [
    PromptVariant(
        name="executive_summary",
        system="You produce executive summaries in 3-5 sentences focusing on main points and conclusions.",
        user_template="Summarize the following text:\n\n{text}\n\nConstraints: 3-5 sentences, focus on key points and conclusions."
    ),
    PromptVariant(
        name="key_takeaways",
        system="You extract key takeaways as bullet points, avoiding fluff.",
        user_template="Summarize into 5-7 bullet-point takeaways:\n\n{text}"
    ),
    PromptVariant(
        name="tl_dr",
        system="You are ultra-brief. Provide a TL;DR in one or two sentences.",
        user_template="TL;DR of the following:\n\n{text}"
    ),
]

# 3) Creative Generation
CREATIVE_GENERATION_VARIANTS: List[PromptVariant] = [
    PromptVariant(
        name="story_warm",
        system="You are a creative storyteller; warm, vivid, and concise.",
        user_template="Write a 200-300 word short story based on this idea: {prompt}"
    ),
    PromptVariant(
        name="poem_minimalist",
        system="You are a modern poet; minimalist and evocative.",
        user_template="Compose a short free-verse poem (8-12 lines) about: {prompt}"
    ),
    PromptVariant(
        name="scifi_pitch",
        system="You are a sci-fi idea generator; punchy and high-concept.",
        user_template="Generate 3 distinct one-paragraph sci-fi novel pitches about: {prompt}"
    ),
]

# 4) Advice
ADVICE_VARIANTS: List[PromptVariant] = [
    PromptVariant(
        name="study_tips_structured",
        system="You are a practical coach. Provide steps, not generic platitudes.",
        user_template="Give 7 concrete, actionable tips for: {topic}"
    ),
    PromptVariant(
        name="mentor_tone",
        system="You are an experienced mentor; encouraging but realistic.",
        user_template="Offer advice (max ~200 words) in mentor tone about: {topic}"
    ),
    PromptVariant(
        name="dos_and_donts",
        system="You present Do's and Don'ts clearly.",
        user_template="Give a list of Do's and Don'ts for: {topic}"
    ),
]

FUNCTIONS: Dict[str, List[PromptVariant]] = {
    "answer": ANSWER_QUESTION_VARIANTS,
    "summarize": SUMMARIZE_TEXT_VARIANTS,
    "create": CREATIVE_GENERATION_VARIANTS,
    "advice": ADVICE_VARIANTS,
}
