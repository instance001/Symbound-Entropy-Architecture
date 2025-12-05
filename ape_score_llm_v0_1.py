
import json
from datetime import datetime
import os
from textwrap import dedent


def call_llm(prompt: str) -> str:
    """
    Stub for an LLM call.

    Replace this with a real call to your local or remote model, e.g.:
    - GPT-OSS
    - local DeepSeek
    - OpenAI-compatible endpoint
    - anything that takes a prompt and returns text

    The function should return the raw text response from the model.
    """
    raise NotImplementedError(
        "Implement call_llm(prompt) to connect this script to your LLM of choice."
    )


RUBRIC = dedent("""
You are a careful cognitive rater following the Cognitive Genome – ApeTest v0.1 rubric.

You will be given:
- A set of 5 probe responses from one person.
- Clear definitions of each structural trait (EUC).

Your job is to:
1) Assign labels for each EUC from the allowed set.
2) Keep your reasoning concise and structured.
3) Output a STRICT JSON object with fields:

{
  "RecursionDepth": "Shallow | Medium | Deep | VeryDeep",
  "RepresentationPreference": ["Verbal", "SpatialMechanical", "Narrative", "Procedural", "Metaphorical"],
  "CompressionStyle": ["Structure", "Detail", "Pattern", "Narrative", "EmotionalImpact"],
  "AmbiguityTolerance": "Low | Medium | High",
  "OverloadFailureMode": "Scatter | Freeze | Loop | Oversimplify"
}

Rules:
- For RepresentationPreference and CompressionStyle, you may choose 1 or 2 labels.
- For all others, choose exactly 1 label.
- If you are unsure, choose the closest match based on the descriptions.

Now, here is the detailed rubric:

RecursionDepth:
- Shallow: Only mentions farms changing (C) with no clear downstream effects.
- Medium: Mentions some downstream effects (e.g., prices) but not the full chain.
- Deep: Tracks food → prices → affordability in the city.
- VeryDeep: Tracks the chain plus ripple effects (e.g., migration, policy, feedback).

RepresentationPreference:
- Verbal: Parts-based, naming components (wheels, frame, chain, etc.).
- SpatialMechanical: How forces and motion flow through the system.
- Narrative: Scenario or story of someone using the bicycle.
- Procedural: Step-by-step instructions for using it.
- Metaphorical: Primarily framed as a comparison to something else.

CompressionStyle:
- Structure: Focus on workflow, organization, or systems.
- Detail: Focus on concrete items and specifics.
- Pattern: Focus on chaos vs order or similar patterns.
- Narrative: Focus on the chef as a character and their actions.
- EmotionalImpact: Focus on stress, calm, or emotional tone.

AmbiguityTolerance:
- Low: Blocks without clearer definition, or insists nothing can be done.
- Medium: Asks clarifying questions or seeks more information as a first move.
- High: Proposes an exploration or mapping approach immediately despite fuzziness.

OverloadFailureMode:
- Scatter: Touches many tasks with little structure; jumps around.
- Freeze: Expresses paralysis or inability to start.
- Loop: Fixates on one or two tasks, repeating them.
- Oversimplify: Collapses complexity to "just start at the top" or similar.
""")


def build_prompt(raw_record: dict) -> str:
    responses = raw_record.get("responses", {})
    return dedent(f"""
    {RUBRIC}

    Here are the probe responses from one person:

    PROBE 1 – Recursion Depth Tolerance:
    {responses.get("probe_1_recursion", "").strip() or "[empty]"}

    PROBE 2 – Representation Preference:
    {responses.get("probe_2_representation", "").strip() or "[empty]"}

    PROBE 3 – Compression Style (one-sentence summary):
    {responses.get("probe_3_compression", "").strip() or "[empty]"}

    PROBE 4 – Ambiguity Tolerance:
    {responses.get("probe_4_ambiguity", "").strip() or "[empty]"}

    PROBE 5 – Overload Failure Mode:
    {responses.get("probe_5_overload", "").strip() or "[empty]"}

    Now respond ONLY with a valid JSON object, no commentary.
    """)


def main():
    print("🧬 Cognitive Genome – ApeTest v0.1 LLM Scoring Layer\n")
    path = input("Enter path to raw responses JSON file: ").strip()
    if not path:
        print("No file path provided. Exiting.")
        return
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    prompt = build_prompt(raw)

    # Call your LLM here
    llm_output = call_llm(prompt)

    try:
        eucs = json.loads(llm_output)
    except json.JSONDecodeError:
        print("\n❌ LLM output was not valid JSON. Raw output:")
        print(llm_output)
        return

    subject_id = raw.get("subject_id", "unknown")

    profile = {
        "version": "CognitiveGenome_v0.1",
        "subject_id": subject_id,
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "eucs": eucs,
        "notes": {
            "free_text": "",
            "rubric": "Scored using Cognitive Genome – ApeTest v0.1 LLM rubric.",
        },
        "source_raw_file": os.path.abspath(path),
    }

    out_name = f"cognitive_genome_profile_llm_{subject_id}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.json"
    with open(out_name, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)

    print(f"\n✅ LLM-scored profile saved to: {out_name}\n")
    print("EUCS:")
    print(json.dumps(profile["eucs"], indent=2))


if __name__ == "__main__":
    main()
