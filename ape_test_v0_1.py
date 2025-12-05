
import json
from datetime import datetime
import uuid


def prompt_multiline(message: str) -> str:
    print(message)
    print("\n(When you're done, press ENTER on an empty line.)\n")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def run_ape_test():
    print("""\
🧬 Cognitive Genome – ApeTest v0.1
---------------------------------
This is an experimental cognitive mapping exercise.
It is NOT a test of intelligence, and it is NOT medical.
It simply tries to understand HOW you think, not HOW WELL you think.
""")

    subject_id = input("Optional: Enter a subject ID or name (or leave blank for random): ").strip()
    if not subject_id:
        subject_id = f"anon-{uuid.uuid4().hex[:8]}"

    responses = {}

    # Probe 1 – Recursion Depth
    responses["probe_1_recursion"] = prompt_multiline(
        "PROBE 1 – Recursion Depth Tolerance\n"
        "Read this chain:\n\n"
        "A) The town builds a new dam.\n"
        "B) The dam changes how much water reaches the farms.\n"
        "C) The farms change how much food reaches the city.\n"
        "D) The amount of food in the city changes food prices.\n"
        "E) Food prices change how many people can afford to live in the city.\n\n"
        "Now imagine C changes – the farms suddenly produce much less food.\n\n"
        "In your own words: What happens next, and why?"
    )

    # Probe 2 – Representation Preference
    responses["probe_2_representation"] = prompt_multiline(
        "PROBE 2 – Representation Preference\n"
        "Explain how a bicycle works to someone who has never seen one.\n"
        "Use whatever style feels most natural to you."
    )

    # Probe 3 – Compression Style
    story = (
        "A chef walks into a busy restaurant kitchen and sees chaos.\n"
        "Pots are boiling over, ingredients are scattered across the benches,\n"
        "staff are bumping into each other, and orders are piling up unread.\n"
        "The chef claps their hands, takes a deep breath, and starts rearranging stations,\n"
        "assigning roles, and clearing space so the kitchen can actually function."
    )
    print("PROBE 3 – Compression Style\n\nHere is the story:\n")
    print(story)
    responses["probe_3_compression"] = input(
        "\nSummarise this story in ONE sentence, in your own words:\n> "
    ).strip()

    # Probe 4 – Ambiguity Tolerance
    responses["probe_4_ambiguity"] = prompt_multiline(
        "PROBE 4 – Ambiguity Tolerance\n"
        "You’re hired to 'improve the system' at a company.\n"
        "Nobody will tell you what 'the system' is yet.\n\n"
        "What is the very first thing you do, and why?"
    )

    # Probe 5 – Overload Failure Mode
    responses["probe_5_overload"] = prompt_multiline(
        "PROBE 5 – Overload Failure Mode\n"
        "You’re given these 10 tasks at once:\n"
        "  1. Answer 30 unread emails\n"
        "  2. Prepare a slide deck\n"
        "  3. Fix a small but urgent bug\n"
        "  4. Plan a birthday dinner\n"
        "  5. Clean your desk\n"
        "  6. Review a long document\n"
        "  7. Call your internet provider\n"
        "  8. Organize your files\n"
        "  9. Schedule three appointments\n"
        "  10. Learn a new software tool\n\n"
        "You have 30 seconds to plan what you’d do. Don’t overthink it.\n\n"
        "Write down what you would do next and in what order:"
    )

    record = {
        "version": "CognitiveGenome_v0.1_raw_responses",
        "subject_id": subject_id,
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "responses": responses,
        "notes": {
            "info": (
                "These are raw probe responses. EUC labels (RecursionDepth, "
                "RepresentationPreference, CompressionStyle, AmbiguityTolerance, "
                "OverloadFailureMode) should be assigned by a scoring layer using "
                "the ApeTest_v0.1 rubric."
            )
        },
    }

    filename = f"cognitive_genome_raw_{subject_id}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)

    print("\n✅ Done! Raw responses saved to:", filename)
    print(
        "\nNext step: run these responses through a scoring tool or LLM using "
        "the Cognitive Genome – ApeTest v0.1 rubric to generate the EUC profile."
    )


if __name__ == "__main__":
    run_ape_test()
