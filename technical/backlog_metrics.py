from dataclasses import dataclass

@dataclass
class WorkItem:
    key: str
    priority: str
    effort: int
    done: bool

WEIGHT = {"critical": 4, "high": 3, "medium": 2, "low": 1}

def prioritize(items):
    return sorted(items, key=lambda x: (WEIGHT.get(x.priority.lower(), 0), -x.effort), reverse=True)

def completion_rate(items):
    return sum(x.done for x in items) / len(items) * 100 if items else 0

if __name__ == "__main__":
    items = [
        WorkItem("INC-101", "Critical", 3, True),
        WorkItem("CHG-204", "High", 5, False),
        WorkItem("IMP-310", "Medium", 8, False),
        WorkItem("BUG-411", "High", 2, True),
    ]
    for item in prioritize(items):
        print(item.key, item.priority, item.effort)
    print(f"Completion rate: {completion_rate(items):.1f}%")
