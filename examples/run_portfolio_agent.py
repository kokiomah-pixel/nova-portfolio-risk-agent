from src.nova_client import get_context
from src.portfolio_policy import decide_portfolio_posture


def main():
    ctx = get_context(asset="portfolio", intent="rebalance", size=100000)
    action = decide_portfolio_posture(ctx)

    print("Regime:", ctx.get("regime"))
    print("Guardrail:", ctx.get("guardrail", {}).get("advisory"))
    print("Portfolio posture:", action)


if __name__ == "__main__":
    main()
