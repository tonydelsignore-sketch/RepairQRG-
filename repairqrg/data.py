"""Sample quick reference data for common repairs."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Sequence


@dataclass(frozen=True)
class RepairStep:
    """A single step in a repair procedure."""

    instruction: str
    tips: Sequence[str] = field(default_factory=tuple)


@dataclass(frozen=True)
class RepairProcedure:
    """Representation of a repair workflow for a specific symptom."""

    name: str
    summary: str
    estimated_time: str
    difficulty: str
    tools: Sequence[str]
    supplies: Sequence[str]
    steps: Sequence[RepairStep]
    notes: Sequence[str] = field(default_factory=tuple)


@dataclass(frozen=True)
class RepairCategory:
    """Grouping of repairs by equipment type."""

    name: str
    overview: str
    procedures: Sequence[RepairProcedure]


def build_sample_catalog() -> Dict[str, RepairCategory]:
    """Return a catalog with curated repair procedures."""

    return {
        "appliances": RepairCategory(
            name="Appliances",
            overview=(
                "Troubleshooting steps for residential appliances covering "
                "symptoms, tools, and procedural tips."
            ),
            procedures=[
                RepairProcedure(
                    name="Refrigerator Not Cooling",
                    summary="Diagnose airflow, condenser, and refrigerant problems.",
                    estimated_time="45-90 minutes",
                    difficulty="Intermediate",
                    tools=(
                        "Phillips screwdriver",
                        "Nut driver",
                        "Multimeter",
                        "Soft brush",
                        "Vacuum cleaner",
                    ),
                    supplies=("Replacement condenser fan", "Coil cleaning spray"),
                    steps=(
                        RepairStep(
                            "Confirm that the thermostat is set below 40°F and the unit has power.",
                            tips=(
                                "Listen for the compressor turning on and off.",
                                "Ensure the plug is firmly seated in the outlet.",
                            ),
                        ),
                        RepairStep(
                            "Inspect condenser coils and clean any accumulated dust with the brush and vacuum.",
                            tips=(
                                "Unplug the appliance before cleaning.",
                                "Clean the coils in the rear and underneath the fridge.",
                            ),
                        ),
                        RepairStep(
                            "Check the condenser fan for obstructions and verify it spins freely.",
                            tips=("Replace the fan if the blades wobble or the motor hums loudly.",),
                        ),
                        RepairStep(
                            "Test the start relay and overload protector using the multimeter.",
                            tips=("Replace components showing infinite resistance.",),
                        ),
                        RepairStep(
                            "Reassemble panels and monitor temperatures for 24 hours.",
                            tips=("Record temperatures at 4-hour intervals to confirm stability.",),
                        ),
                    ),
                    notes=(
                        "If the compressor is not running, evaluate refrigerant pressure with certified equipment.",
                        "Document serial numbers for warranty verification before ordering parts.",
                    ),
                ),
                RepairProcedure(
                    name="Dishwasher Leaking",
                    summary="Identify leaks caused by seals, hoses, or incorrect loading.",
                    estimated_time="30-60 minutes",
                    difficulty="Beginner",
                    tools=("Torx screwdriver", "Flashlight", "Replacement gasket"),
                    supplies=("Dishwasher-safe cleaner", "Absorbent towels"),
                    steps=(
                        RepairStep(
                            "Inspect the door gasket for tears and remove debris from the seal channel.",
                            tips=("Allow the gasket to soak in warm water before reinstalling.",),
                        ),
                        RepairStep(
                            "Verify the float switch moves freely and is not obstructed by dishes.",
                        ),
                        RepairStep(
                            "Run a short cycle while observing the inlet hose and pump housing for drips.",
                            tips=(
                                "Keep towels around the unit to quickly soak leaks.",
                                "Tighten hose clamps gently to avoid cracking plastic fittings.",
                            ),
                        ),
                        RepairStep(
                            "Check leveling feet to ensure the tub sits evenly and adjust as needed.",
                        ),
                    ),
                    notes=(
                        "Use manufacturer-specific gaskets for a reliable seal.",
                        "Recommend routine cleaning cycles every 30 days to prevent buildup.",
                    ),
                ),
            ],
        ),
        "electronics": RepairCategory(
            name="Consumer Electronics",
            overview="Quick diagnostics for smartphones, laptops, and televisions.",
            procedures=[
                RepairProcedure(
                    name="Smartphone Won't Charge",
                    summary="Resolve charging issues caused by cables, ports, or batteries.",
                    estimated_time="15-45 minutes",
                    difficulty="Beginner",
                    tools=("Soft brush", "Plastic spudger", "Replacement charging port"),
                    supplies=("Isopropyl alcohol", "Compressed air"),
                    steps=(
                        RepairStep(
                            "Inspect the charging cable and power brick for damage and test with a known-good set.",
                        ),
                        RepairStep(
                            "Use compressed air and the soft brush to clean lint from the charging port.",
                            tips=(
                                "Hold the phone at a downward angle to encourage debris to fall out.",
                            ),
                        ),
                        RepairStep(
                            "Enter safe mode or power cycle the phone to rule out software issues.",
                        ),
                        RepairStep(
                            "Disassemble the device using the spudger to access the charging port.",
                            tips=(
                                "Track screw placement using a magnetic pad or template.",
                            ),
                        ),
                        RepairStep(
                            "Replace the charging port assembly, reconnecting ribbon cables securely.",
                        ),
                    ),
                    notes=(
                        "Advise the customer to test charging with multiple outlets before returning the device.",
                        "Back up data prior to disassembly if possible.",
                    ),
                ),
                RepairProcedure(
                    name="Laptop Overheating",
                    summary="Improve airflow and thermal efficiency for laptops running hot.",
                    estimated_time="40-75 minutes",
                    difficulty="Intermediate",
                    tools=("Precision screwdriver set", "Thermal paste", "ESD wrist strap"),
                    supplies=("Compressed air", "Lint-free cloth"),
                    steps=(
                        RepairStep(
                            "Document the overheating symptoms and confirm they occur under typical workloads.",
                        ),
                        RepairStep(
                            "Open the chassis and disconnect the battery using the ESD strap.",
                        ),
                        RepairStep(
                            "Use compressed air to clear dust from fans, vents, and heatsinks.",
                            tips=(
                                "Hold the fan blades steady to avoid back-spinning the motor.",
                            ),
                        ),
                        RepairStep(
                            "Remove the heatsink, clean old thermal paste, and apply a pea-sized amount of new paste.",
                        ),
                        RepairStep(
                            "Reassemble the laptop, ensuring all cables are reconnected, and run a stress test.",
                        ),
                    ),
                    notes=(
                        "Log pre- and post-repair temperatures to demonstrate improvement.",
                        "Check for BIOS updates that improve fan curves.",
                    ),
                ),
            ],
        ),
        "hvac": RepairCategory(
            name="HVAC",
            overview="Field guide for residential HVAC service calls.",
            procedures=[
                RepairProcedure(
                    name="Furnace Ignition Failure",
                    summary="Restore ignition by verifying power, sensors, and gas supply.",
                    estimated_time="30-90 minutes",
                    difficulty="Advanced",
                    tools=(
                        "Multimeter",
                        "Manometer",
                        "Wire brush",
                        "Allen wrench set",
                        "Vacuum",
                    ),
                    supplies=("Replacement flame sensor", "Compressed air duster"),
                    steps=(
                        RepairStep(
                            "Shut off power to the furnace and remove the access panel.",
                        ),
                        RepairStep(
                            "Check for diagnostic blink codes and note any error sequences.",
                            tips=("Keep a photo log of codes for customer records.",),
                        ),
                        RepairStep(
                            "Measure voltage at the control board to confirm power delivery.",
                        ),
                        RepairStep(
                            "Clean or replace the flame sensor using the wire brush.",
                        ),
                        RepairStep(
                            "Verify gas pressure with the manometer and relight the furnace.",
                        ),
                    ),
                    notes=(
                        "Document combustion readings before leaving the job site.",
                        "Test the thermostat for loose connections.",
                    ),
                ),
                RepairProcedure(
                    name="Air Conditioner Low Airflow",
                    summary="Diagnose poor airflow due to filters, coils, or blower issues.",
                    estimated_time="25-60 minutes",
                    difficulty="Beginner",
                    tools=("Screwdriver", "Fin comb", "Shop vacuum"),
                    supplies=("Replacement air filter", "Coil cleaner"),
                    steps=(
                        RepairStep(
                            "Inspect and replace dirty air filters, ensuring correct orientation.",
                        ),
                        RepairStep(
                            "Vacuum the evaporator coil housing and gently clean the fins with the comb.",
                        ),
                        RepairStep(
                            "Check the blower wheel for debris and tighten set screws if loose.",
                        ),
                        RepairStep(
                            "Confirm dampers are open and registers unobstructed throughout the home.",
                        ),
                    ),
                    notes=(
                        "Educate customers on filter replacement schedules.",
                        "If airflow remains low, evaluate duct static pressure.",
                    ),
                ),
            ],
        ),
    }


def flatten_procedures(catalog: Dict[str, RepairCategory]) -> Iterable[RepairProcedure]:
    """Yield all procedures from the provided catalog."""

    for category in catalog.values():
        yield from category.procedures
