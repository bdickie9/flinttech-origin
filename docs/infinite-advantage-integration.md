# FLINTTECH Infinite Advantage integration gate

## Current evidence

The local v4 artifact has 21 passing Python unittest tests, including API authentication, workflow transitions, and dashboard serving. This is **not** proof of production readiness. The v4 source has not yet been committed to this repository, so this document does not claim an integrated deployment.

## Release criteria (all required)

1. Commit the audited `flintcore` source, tests, Dockerfile and static assets to a dedicated application directory in a reviewable PR. Never commit `.env` files or secrets.
2. CI must run `python -m unittest discover -s tests -v`, Python compilation, static checks, dependency scanning, and Docker image build on the committed application.
3. Reject production startup without distinct high-entropy API and approval secrets. Authenticate the operator who issues approvals; implement expiry and revocation.
4. Protect all nonpublic endpoints, constrain request sizes, apply rate limiting, and run a security review of the HTTP server, storage, and browser UI.
5. Use durable encrypted storage and off-host audit checkpoints; prove restore and tamper-detection behavior.
6. Integrate payment processors in **read-only** mode first. Reconcile account, currency, amount, transaction ID, settlement/refund status and fees. Never equate `sold` with collected funds.
7. Exercise checkout and fulfillment using sandbox events and signed webhooks, then a separately authorized production transaction.
8. Confirm actual customer consent, fulfillment, revenue and costs with independent evidence. Never invent customer outcomes.
9. Keep deployment, transfers, refunds, account changes and customer outreach behind explicit authorization.
10. Record deployment URL, commit SHA, health check, rollback procedure, and evidence that production behavior matches the reviewed artifact.

## Current hold

**HOLD: not deployable as a revenue-producing autonomous service.** Local v4 testing alone cannot establish live payments, identity-based approvals, secure public exposure or fulfilled orders.

## Next measurable action

Import the v4 application source into this branch, run CI against that exact commit, and review security gaps before requesting merge. No claims of production revenue or autonomous completion are authorized by this document.
