import sys

def calculate_itil_priority(impact, urgency):
    """
    ITIL 4 Standard Priority Calculation Matrix
    Impact & Urgency levels: 1 = High, 2 = Medium, 3 = Low
    """
    matrix = {
        (1, 1): "P1 - Critical (Immediate escalation)",
        (1, 2): "P2 - High (Target resolution: 4h)",
        (1, 3): "P3 - Medium (Target resolution: 8h)",
        (2, 1): "P2 - High (Target resolution: 4h)",
        (2, 2): "P3 - Medium (Target resolution: 8h)",
        (2, 3): "P4 - Low (Target resolution: 24h)",
        (3, 1): "P3 - Medium (Target resolution: 8h)",
        (3, 2): "P4 - Low (Target resolution: 24h)",
        (3, 3): "P5 - Planning (Scheduled resolution)",
    }
    
    return matrix.get((impact, urgency), "Unknown Level")

if __name__ == "__main__":
    print("[*] ITIL 4 Incident Triage Utility Initialized.")
    # Example: Major outage affecting corporate AI API Gateway (High Impact, High Urgency)
    priority = calculate_itil_priority(1, 1)
    print(f"[+] Incident Triage Status: {priority}")
