def next_status(current):
    flow = ["Submitted", "KYC Verified", "Under Review", "Approved", "Rejected"]
    if current in flow and current != "Rejected":
        return flow[min(flow.index(current) + 1, len(flow)-1)]
    return current
