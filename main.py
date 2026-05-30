# =========================
# UNIFIED INFORMATION CORE
# Quantum + Physics + Genome
# =========================

import math
import random


# =========================
# CORE: INFO FIELD
# =========================

class InfoField:
    def __init__(self, data, domain):
        self.data = data
        self.domain = domain

    def to_bits(self):
        return "".join(format(ord(c), "08b") for c in str(self.data))


# =========================
# ENTROPY ENGINE
# =========================

def entropy_from_string(data):
    freq = {}
    for c in str(data):
        freq[c] = freq.get(c, 0) + 1

    total = len(str(data))
    probs = [f / total for f in freq.values()]

    return -sum(p * math.log2(p) for p in probs if p > 0)


# =========================
# QUANTUM MODULE (SIMULATED)
# =========================

class QuantumState:
    def __init__(self, p0=0.5, p1=0.5):
        self.state = {"0": p0, "1": p1}

    def measure(self):
        return "0" if self.state["0"] >= self.state["1"] else "1"

    def collapse_entropy(self):
        return -sum(p * math.log2(p) for p in self.state.values() if p > 0)


# =========================
# PHYSICS MODULE (INFO ENERGY MODEL)
# =========================

class PhysicsState:
    def __init__(self, energy, info):
        self.energy = energy
        self.info = info

    def landauer_cost(self):
        return self.info * 1.6e-19

    def efficiency(self):
        return self.energy / (self.landauer_cost() + 1e-12)


# =========================
# GENOME MODULE
# =========================

class GenomeState:
    def __init__(self, sequence):
        self.sequence = sequence

    def mutate(self, rate=0.1):
        bases = ["A", "T", "C", "G"]
        seq = list(self.sequence)

        for i in range(len(seq)):
            if random.random() < rate:
                seq[i] = random.choice(bases)

        return GenomeState("".join(seq))

    def complexity(self):
        return len(set(self.sequence))


# =========================
# TRANSFORMER (UNIFIED CORE)
# =========================

class Transformer:
    def transform(self, field: InfoField):
        data = str(field.data)

        return {
            "domain": field.domain,
            "original": data,
            "reversed": data[::-1],
            "entropy": entropy_from_string(data),
            "bits": field.to_bits()
        }


# =========================
# ROUTER (DOMAIN SELECTOR)
# =========================

class Router:
    def route(self, task: str):
        t = task.lower()

        if any(x in t for x in ["qubit", "quantum", "superposição"]):
            return "quantum"

        if any(x in t for x in ["energia", "entropia", "informação"]):
            return "physics"

        if any(x in t for x in ["dna", "genoma", "gene"]):
            return "genome"

        return "general"


# =========================
# UNIFIED ENGINE
# =========================

class UnifiedEngine:
    def __init__(self):
        self.router = Router()
        self.transformer = Transformer()

    def process(self, task, data):
        domain = self.router.route(task)

        field = InfoField(data, domain)
        transformed = self.transformer.transform(field)

        if domain == "quantum":
            q = QuantumState()
            return {
                "domain": "quantum",
                "measurement": q.measure(),
                "collapse_entropy": q.collapse_entropy(),
                "info": transformed
            }

        if domain == "physics":
            p = PhysicsState(energy=10, info=len(str(data)))
            return {
                "domain": "physics",
                "efficiency": p.efficiency(),
                "landauer_cost": p.landauer_cost(),
                "info": transformed
            }

        if domain == "genome":
            g = GenomeState(str(data))
            mutated = g.mutate()
            return {
                "domain": "genome",
                "complexity": g.complexity(),
                "mutated": mutated.sequence,
                "info": transformed
            }

        return {
            "domain": "general",
            "info": transformed
        }


# =========================
# MAIN EXECUTION
# =========================

if __name__ == "__main__":
    engine = UnifiedEngine()

    task = input("Task: ")
    data = input("Data: ")

    result = engine.process(task, data)

    print("\n--- RESULT ---")
    for k, v in result.items():
        print(f"{k}: {v}")