
import json
from datetime import datetime
import os


def choose_option(prompt, options, allow_multi=False):
    print(prompt)
    for i, (key, desc) in enumerate(options.items(), start=1):
        print(f"  {i}. {key} – {desc}")
    if allow_multi:
        raw = input("\nEnter one or two option numbers (comma-separated): ").strip()
        if not raw:
            return []
        result = []
        for part in raw.split(","):
            part = part.strip()
            if not part.isdigit():
                continue
            idx = int(part) - 1
            if 0 <= idx < len(options):
                result.append(list(options.keys())[idx])
        return result
    else:
        while True:
            raw = input("\nEnter option number: ").strip()
            if not raw.isdigit():
                print("Please enter a number.")
                continue
            idx = int(raw) - 1
            if 0 <= idx < len(options):
                return list(options.keys())[idx]
            print("Invalid choice, try again.")


def score_recursion_depth(response_text):
    print("\n=== SCORING: Recursion Depth Tolerance ===")
    print("\nProbe response:")
    print("----------------------------------------")
    print(response_text or "(empty)")
    print("----------------------------------------\n")
    options = {
        "Shallow": "Only mentions farms changing (C) with no clear downstream effects.",
        "Medium": "Mentions some downstream effects (e.g., prices) but not the full chain.",
        "Deep": "Tracks food → prices → affordability in the city.",
        "VeryDeep": "Tracks the chain plus ripple effects (e.g., migration, policy, feedback).",
    }
    return choose_option("Select the best description of the reasoning depth:", options)


def score_representation_pref(response_text):
    print("\n=== SCORING: Representation Preference ===")
    print("\nProbe response:")
    print("----------------------------------------")
    print(response_text or "(empty)")
    print("----------------------------------------\n")
    options = {
        "Verbal": "Parts-based, naming components (wheels, frame, chain, etc.).",
        "SpatialMechanical": "How forces and motion flow through the system.",
        "Narrative": "Scenario or story of someone using the bicycle.",
        "Procedural": "Step-by-step instructions for using it.",
        "Metaphorical": "Primarily framed as a comparison to something else.",
    }
    return choose_option(
        "Select one or two dominant representation styles:", options, allow_multi=True
    )


def score_compression_style(response_text):
    print("\n=== SCORING: Compression Style ===")
    print("\nProbe response (one-sentence summary):")
    print("----------------------------------------")
    print(response_text or "(empty)")
    print("----------------------------------------\n")
    options = {
        "Structure": "Focus on workflow, organization, or systems.",
        "Detail": "Focus on concrete items (pots, ingredients, staff, etc.).",
        "Pattern": "Focus on chaos vs order or similar patterns.",
        "Narrative": "Focus on the chef as a character and their actions.",
        "EmotionalImpact": "Focus on stress, calm, or emotional tone.",
    }
    return choose_option(
        "Select one or two dominant compression styles:", options, allow_multi=True
    )


def score_ambiguity_tolerance(response_text):
    print("\n=== SCORING: Ambiguity Tolerance ===")
    print("\nProbe response:")
    print("----------------------------------------")
    print(response_text or "(empty)")
    print("----------------------------------------\n")
    options = {
        "Low": "Blocks without clearer definition, or insists nothing can be done.",
        "Medium": "Asks clarifying questions or seeks more information as a first move.",
        "High": "Proposes an exploration or mapping approach immediately despite fuzziness.",
    }
    return choose_option("Select the best fit for their first move under ambiguity:", options)


def score_overload_failure_mode(response_text):
    print("\n=== SCORING: Overload Failure Mode ===")
    print("\nProbe response:")
    print("----------------------------------------")
    print(response_text or "(empty)")
    print("----------------------------------------\n")
    options = {
        "Scatter": "Touches many tasks with little structure; jumps around.",
        "Freeze": "Expresses paralysis or inability to start.",
        "Loop": "Fixates on one or two tasks, repeating them.",
        "Oversimplify": "Collapses complexity to 'just start at the top' or similar.",
    }
    return choose_option("Select the dominant pattern under load:", options)


def main():
    print("🧬 Cognitive Genome – ApeTest v0.1 Scoring Layer\n")
    path = input("Enter path to raw responses JSON file: ").strip()
    if not path:
        print("No file path provided. Exiting.")
        return
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    responses = raw.get("responses", {})
    subject_id = raw.get("subject_id", "unknown")

    # Score each EUC
    recursion = score_recursion_depth(responses.get("probe_1_recursion", ""))
    rep_pref = score_representation_pref(responses.get("probe_2_representation", ""))
    compression = score_compression_style(responses.get("probe_3_compression", ""))
    ambiguity = score_ambiguity_tolerance(responses.get("probe_4_ambiguity", ""))
    overload = score_overload_failure_mode(responses.get("probe_5_overload", ""))

    # Optional notes
    print("\n(Optional) Add any free-form notes about this profile (or leave blank):")
    free_notes = input("> ").strip()

    # Build profile
    profile = {
        "version": "CognitiveGenome_v0.1",
        "subject_id": subject_id,
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "eucs": {
            "RecursionDepth": recursion,
            "RepresentationPreference": rep_pref,
            "CompressionStyle": compression,
            "AmbiguityTolerance": ambiguity,
            "OverloadFailureMode": overload,
        },
        "notes": {
            "free_text": free_notes,
            "rubric": "Scored using Cognitive Genome – ApeTest v0.1 manual rubric.",
        },
        "source_raw_file": os.path.abspath(path),
    }

    out_name = f"cognitive_genome_profile_{subject_id}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.json"
    with open(out_name, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Profile saved to: {out_name}\n")
    print("Summary:")
    print(json.dumps(profile["eucs"], indent=2))


if __name__ == "__main__":
    main()
