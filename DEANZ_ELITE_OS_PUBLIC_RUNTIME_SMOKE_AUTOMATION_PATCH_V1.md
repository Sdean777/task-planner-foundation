# Dean'z Elite OS Public Runtime Smoke Automation Patch v1

## Purpose

This document records the first bounded patch that creates a separate
read-only public runtime smoke workflow for the `task-planner-foundation`
service.

It exists to answer these questions:

- what exact workflow file was created?
- how does it remain read-only and separate from deployment authority?
- what does it prove without widening AWS or rollout power?

This patch does not:

- modify `.github/workflows/deploy-foundation-skeleton.yml`
- change `app.py`
- add AWS authentication
- add schedule triggers
- add rollback logic

## Scope

This patch applies only to:

- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_CONTROLLED_PATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PROPOSAL_V1.md)
- [`.github/workflows/public-runtime-smoke.yml`](./.github/workflows/public-runtime-smoke.yml)
- [`.github/public-runtime-smoke-automation-patch.template.json`](./.github/public-runtime-smoke-automation-patch.template.json)

It governs only the new read-only smoke workflow file.

## Patch Result

This mission created exactly one new workflow file:

- [`.github/workflows/public-runtime-smoke.yml`](./.github/workflows/public-runtime-smoke.yml)

The workflow remains bounded:

- trigger: `workflow_dispatch` only
- workflow-level permissions: `contents: read`
- one job only: `public-runtime-smoke`
- one non-secret input source:
  - `vars.FOUNDATION_PUBLIC_BASE_URL`
- one derived variable:
  - `PUBLIC_BASE_URL`
- three smoke rounds at five-second spacing
- read-only shell commands only:
  - `curl`
  - `jq`
  - `sleep`
- summary-only outcome reporting

## Read-Only Proof

The workflow does not contain:

- `schedule`
- `workflow_run`
- `push`
- `pull_request`
- `aws-actions/configure-aws-credentials`
- `aws` commands
- `docker` commands
- rollback logic
- hardcoded live public URLs

That keeps the smoke workflow separate from deployment authority.

## Preserved Boundaries

This patch preserved the important boundaries:

- `.github/workflows/deploy-foundation-skeleton.yml` stayed unchanged
- `app.py` stayed unchanged
- no AWS mutation happened in this mission
- no secrets or credentials were added to source
- no deployment authority widened

## Canonical Patch Artifact

The non-secret patch artifact for this mission is:

- [`.github/public-runtime-smoke-automation-patch.template.json`](./.github/public-runtime-smoke-automation-patch.template.json)

## Recommended Next Mission

The next bounded step after this patch should be:

- `GitHub-Hosted Public Runtime Smoke Workflow Dispatch Review v1`

That mission should decide whether the now-proven read-only smoke workflow is
ready for repository-backed hosted execution without widening triggers,
permissions, or deployment authority.
