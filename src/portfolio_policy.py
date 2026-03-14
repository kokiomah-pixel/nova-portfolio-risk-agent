def decide_portfolio_posture(ctx: dict) -> str:
    regime = ctx.get("regime")
    severity = ctx.get("guardrail", {}).get("severity")

    if regime == "Stress":
        return "reduce_risk"

    if regime == "Elevated Fragility":
        return "tighten_exposure"

    if severity == "high":
        return "reduce_exposure"

    return "proceed"
