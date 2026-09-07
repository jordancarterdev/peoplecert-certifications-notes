from dataclasses import dataclass
from statistics import mean

@dataclass
class ServiceCheck:
    service: str
    latency_ms: float
    available: bool

def availability(checks):
    return sum(x.available for x in checks) / len(checks) * 100 if checks else 0.0

def average_latency(checks):
    return round(mean(x.latency_ms for x in checks), 2) if checks else 0.0

if __name__ == "__main__":
    checks = [
        ServiceCheck("Collaboration", 84, True),
        ServiceCheck("Identity", 92, True),
        ServiceCheck("Business App", 131, True),
        ServiceCheck("Endpoint", 178, False),
    ]
    print(f"Availability: {availability(checks):.2f}%")
    print(f"Average latency: {average_latency(checks):.2f} ms")
