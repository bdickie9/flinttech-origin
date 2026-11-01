# Engineering Case Study: Why FLINTTECH Changed Its Checkout Design

**Author:** Bradley Dickover, Founder of FLINTTECH  
**Status:** Engineering case study; source-level fixes committed, production verification pending  
**Date:** November 1, 2026

## The problem

A review of the FLINTTECH APEX go-to-market application identified three connected risks in its Metro Permit Leads subscription workflow:

1. The customer-facing page described a $299 monthly subscription, while the revenue catalog documented $199.
2. An unexpected checkout error could redirect customers to a static Stripe Payment Link that did not enforce the selected exclusive territory.
3. Territory availability relied on eventually consistent Stripe subscription search, which cannot guarantee exclusive allocation under concurrent purchases.

The product also had conflicting statements about whether St. Paul was ready for fulfillment.

## The engineering response

The APEX repair branch replaces the unsafe fallback with a visible checkout error, aligns the page copy to the documented $199 price, and marks St. Paul unavailable pending data-feed verification.

A subsequent safety change makes exclusive-territory checkout fail closed until a durable, atomic reservation service is implemented. This prevents the proposed code path from accepting payment without a reliable inventory guarantee, at the cost of temporarily blocking that sale.

Regression assertions were committed to the branch. Their successful execution and full production integration have not been established.

## Why the distinction matters

A successful payment is not proof of fulfillment. An active subscription is not an atomic inventory lock. A repository fix is not a production deployment.

The planned replacement design will bind each checkout to a catalog version, merchant, order, territory reservation, verified payment, and fulfillment record.

## Evidence and limitations

- [APEX safety pull request #21](https://github.com/bdickie9/apex-gtm/pull/21)
- [FLINTTECH founder and engineering portfolio](https://github.com/bdickie9)
- The documented price is not independently verified against the current Stripe merchant account.
- No claim is made that the repaired checkout is deployed or that paid customers have been fulfilled.

## Engineering principle

**A system should never report an external business outcome as verified merely because it attempted the action or recorded a local success.**

This case study documents an identified engineering risk and an ongoing remediation, not a completed production success.
