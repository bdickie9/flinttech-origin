# FLINTTECH Infinite Advantage — integration staging

The complete v11 Python source is available as a local ZIP artifact, **not yet in this GitHub branch**. The 55 local unittests were rerun successfully on 2026-11-16/17. This directory intentionally contains only staging documentation, not a deployable application.

## Source import

Extract the v11 ZIP at repository root, preserving `infinite-advantage/flintcore`, `infinite-advantage/tests`, `infinite-advantage/Dockerfile`, `infinite-advantage/requirements.txt` and static assets. Avoid committing `__pycache__`, SQLite files, environment secrets or generated backups. Run `cd infinite-advantage && python -m unittest discover -s tests -v` and `python -m compileall -q flintcore tests`. Commit source on `feat/infinite-advantage-integration` and require the GitHub Actions check on the exact commit SHA.

Do not merge or deploy until production authentication, payment reconciliation, agent orchestration and independent security review are complete. No revenue or live customer delivery has been verified.
