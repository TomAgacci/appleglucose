#!/usr/bin/env python3
"""
APPLE PULP → GLUCOSE-RICH SYRUP → CIDER → FRUCTOSE-ENRICHED EXTRACT
Interactive terminal guide for the full workflow.

This script:
- Asks for batch sizes.
- Prints detailed step-by-step instructions.
- Pauses between stages so you can run it like a process wizard.
"""

import sys
from textwrap import dedent

def pause(msg="Press ENTER to continue..."):
    input(f"\n{msg}\n")

def ask_float(prompt, default=None):
    while True:
        txt = input(f"{prompt}" + (f" [{default}]" if default is not None else "") + ": ").strip()
        if not txt and default is not None:
            return float(default)
        try:
            return float(txt)
        except ValueError:
            print("Please enter a number.")

def banner():
    print("=" * 80)
    print(" APPLE PULP → GLUCOSE SYRUP → CIDER → FRUCTOSE-ENRICHED EXTRACT ")
    print("=" * 80)
    print(dedent("""
        This wizard walks you through three linked processes:

          1. Make a glucose-rich syrup from apple pulp.
          2. Ferment that syrup into cider.
          3. Enrich the sugar fraction via freeze concentration
             (ice-cider style) and optional gentle reduction.

        NOTE:
          - All outputs are mixed-sugar products (glucose, fructose, sucrose).
          - This does NOT produce isolated pure fructose or HFCS.
    """))

def configure_batch():
    print("\n--- BATCH CONFIGURATION ---")
    pulp_mass = ask_float("Approximate mass of apple pulp (kg)", default=1.0)
    water_ratio = ask_float("Water ratio (parts water per part pulp)", default=1.2)

    slurry_water_mass = pulp_mass * water_ratio

    print("\nCalculated slurry:")
    print(f"  Apple pulp: {pulp_mass:.3f} kg")
    print(f"  Water:      {slurry_water_mass:.3f} kg")

    lemon_per_liter = 1.5  # tablespoons per liter (approx)
    # Rough density assumption: 1 kg ≈ 1 L for slurry
    slurry_volume_l = pulp_mass + slurry_water_mass
    lemon_tbsp = lemon_per_liter * slurry_volume_l

    print(f"\nSuggested lemon juice (acidification): ~{lemon_tbsp:.1f} tablespoons")

    return {
        "pulp_mass": pulp_mass,
        "water_mass": slurry_water_mass,
        "slurry_volume_l": slurry_volume_l,
        "lemon_tbsp": lemon_tbsp,
    }

def syrup_instructions(batch):
    print("\n=== PART 1 — GLUCOSE-RICH SYRUP FROM APPLE PULP ===")
    print(dedent(f"""
        INPUTS:
          - Apple pulp: {batch['pulp_mass']:.3f} kg
          - Water:      {batch['water_mass']:.3f} kg
          - Lemon juice: ~{batch['lemon_tbsp']:.1f} tablespoons (approx.)

        STEP 1 — MAKE SLURRY
          - Add apple pulp to a pot.
          - Add water to form a thick slurry.
          - Stir until uniform.

        STEP 2 — ACIDIFY
          - Add lemon juice (~{batch['lemon_tbsp']:.1f} tbsp total).
          - Goal pH: approx. 3.0–3.5 (no meter required).

        STEP 3 — HEAT FOR HYDROLYSIS
          - Heat slurry to 80–90 °C.
          - Hold for 45–60 minutes.
          - Stir every 5–10 minutes.
          - This extracts native sugars and partially breaks down complex carbs.

        STEP 4 — STRAIN
          - Pour hot slurry through fine mesh / cloth / nut milk bag.
          - Press to extract as much liquid as possible.
          - Collect strained liquid in a clean pot.

        STEP 5 — CONCENTRATE TO SYRUP
          - Heat strained liquid on LOW.
          - Simmer gently; avoid hard boiling.
          - Reduce volume by ~30–60% until syrupy.
          - Cool and transfer to a clean glass jar.

        OUTPUT:
          - GLUCOSE-RICH SYRUP (mixed sugars, but glucose-forward).
    """))
    pause()

def cider_instructions():
    print("\n=== PART 2 — FERMENT GLUCOSE-RICH SYRUP INTO CIDER ===")
    print(dedent("""
        GOAL:
          - Turn your glucose-rich syrup into a fermented cider.

        STEP 1 — DILUTE SYRUP
          - Mix syrup with water to reach ~10–15% sugar by weight.
          - Rough starting point: 1 part syrup to 2–3 parts water.
          - Stir until fully dissolved.

        STEP 2 — COOL & PITCH YEAST
          - Ensure liquid is at room temperature (~20–25 °C).
          - Add wine/cider yeast (or baker’s yeast for simple tests):
            - Typical: 1–5 g yeast per 1–5 L of liquid.
          - Stir gently to distribute.

        STEP 3 — FERMENT
          - Use a fermentation vessel with airlock or loosely fitted lid.
          - Ferment at 18–24 °C.
          - Active fermentation: 3–7 days (visible bubbling).
          - Secondary clearing: 7–14 days (slower activity, sediment forming).
          - When bubbling stops and liquid clears, you have CIDER.

        STEP 4 — RACK (OPTIONAL)
          - Carefully pour cider off the sediment into a clean container.
          - This improves clarity and reduces solids.

        OUTPUT:
          - CIDER made from your glucose-rich syrup.
    """))
    pause()

def enrichment_instructions():
    print("\n=== PART 3 — FRUCTOSE-ENRICHED SUGAR EXTRACT (FREEZE CONCENTRATION) ===")
    print(dedent("""
        GOAL:
          - Enrich the sugar fraction from cider using freeze concentration
            (ice-cider style) and optional gentle reduction.

        METHOD A — FREEZE CONCENTRATION

        STEP 1 — FREEZE
          - Pour finished cider into a freezer-safe container.
          - Freeze solid.

        STEP 2 — SLOW THAW
          - Move frozen cider to the refrigerator.
          - Let it thaw slowly.
          - As it thaws, liquid will drip out first.

        STEP 3 — COLLECT FIRST MELT
          - Collect the first 30–50% of melted liquid.
          - This fraction is higher in sugars and flavor.
          - Remaining ice is mostly water.

        METHOD B — OPTIONAL HEAT REDUCTION

        STEP 4 — REDUCE (OPTIONAL)
          - Take the enriched fraction.
          - Heat gently at 60–70 °C.
          - Evaporate water slowly until syrupy.
          - Avoid boiling hard to prevent caramelization.

        OUTPUT:
          - FRUCTOSE-ENRICHED SUGAR EXTRACT (still a mixed-sugar syrup).
          - Sweet, concentrated, excellent for flavoring or further experiments.

        IMPORTANT:
          - This process enriches fructose relative to the original cider/syrup.
          - It does NOT produce isolated pure fructose or HFCS.
    """))
    pause("Press ENTER to finish the workflow...")

def main():
    banner()
    batch = configure_batch()
    syrup_instructions(batch)
    cider_instructions()
    enrichment_instructions()
    print("\nWorkflow complete.")
    print("You now have a full process guide from pulp → syrup → cider → enriched extract.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
