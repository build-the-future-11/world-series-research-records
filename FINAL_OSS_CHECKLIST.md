# Final open-source checklist (execute)

Status after 26 September 2026 go-live + optional packaging follow-through.

## Required for public OSS — DONE

- [x] Apache-2.0 license grant (`LICENSE`, `NOTICE`, `THIRD_PARTY.md`)
- [x] Public repos under `build-the-future-11`
- [x] Push main + CI green
- [x] Release `v0.1.0-oss` with review archive + SHA-256
- [x] Bounded manuscript + claim digest verify (9/9)
- [x] Restored-source tests/doctor/WFIM/audit verify
- [x] Authorship attestation signed in-repo (`docs/AUTHORSHIP.md`)
- [x] README release/CI/license badges
- [x] `.mailmap` maps placeholder email → GitHub noreply (no git-config change)
- [x] arXiv TeX source bundle prepared at `world-series/paper/arxiv/`

## Human-only remaining

- [ ] Submit the prepared bundle at https://arxiv.org/submit (`paper/arxiv/README.md`)
- [ ] After arXiv assigns an id, add it to README/release notes
- [ ] Optional: set your local git `user.email` to `271452460+build-the-future-11@users.noreply.github.com` for future commits (do this yourself; tools here will not edit git config)

## Out of scope (do not block OSS)

- Independent external confirmation
- E1–E9 stronger scientific campaigns
- Completing all nine original full architectures
