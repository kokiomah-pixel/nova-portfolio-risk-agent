
# Nova Portfolio Risk Agent

A minimal portfolio risk agent example that queries **Sharpe Nova OS** before changing portfolio exposure.

This project demonstrates how allocators and portfolio systems can use Nova decision context to:

- detect elevated fragility
- tighten exposure under unstable conditions
- reduce risk during stress
- preserve disciplined capital posture

Nova does not rebalance portfolios or execute trades.  
Nova provides decision context before portfolio decisions.

---

# What This Repo Shows

This starter shows a simple portfolio decision loop:

1. Evaluate a proposed portfolio posture change
2. Query Nova decision context
3. Evaluate regime and guardrail
4. Decide whether to:
   - proceed
   - tighten exposure
   - reduce risk
   - pause new risk

This is a decision-support example only.

---

# Core Primitive

```python
ctx = nova.context()

ctx = get_context(asset="portfolio", intent="rebalance", size=100000)
action = decide_portfolio_posture(ctx)

print("Regime:", ctx.get("regime"))
print("Guardrail:", ctx.get("guardrail", {}).get("advisory"))
print("Portfolio posture:", action)
