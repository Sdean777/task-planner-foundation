# Dean'z Elite OS Public Runtime Smoke Automation Controlled Patch Review v1

## Purpose

This document defines the first bounded controlled-patch review for a future
read-only public runtime smoke workflow for the `task-planner-foundation`
service.

It exists to answer these questions before any workflow file is created:

- what exact future workflow hunk is reviewable?
- what lines and behaviors must remain unchanged around that hunk?
- what evidence must still be rechecked immediately before a patch?
- how does the future patch remain read-only and separate from deployment
  authority?

This review does not:

- create the workflow file
- modify the deployment workflow
- add AWS authentication
- add schedule triggers
- change the Flask application contract

## Scope

This controlled-patch review applies to:

- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_REVIEW_V1.md)
- [DEANZ_ELITE_OS_POST_DEPLOY_PUBLIC_RUNTIME_SMOKE_TESTS_V1.md](./DEANZ_ELITE_OS_POST_DEPLOY_PUBLIC_RUNTIME_SMOKE_TESTS_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)
- [`.github/public-runtime-smoke-automation-controlled-patch-review.template.json`](./.github/public-runtime-smoke-automation-controlled-patch-review.template.json)

It governs only the exact review boundary for one future read-only smoke
workflow file.

## Controlled Patch Review Objective

This review exists to decide whether the future smoke-automation patch
remains:

- `smoke_automation_controlled_patch_blocked`
- `smoke_automation_controlled_patch_review_required`
- `smoke_automation_controlled_patch_ready_for_patch`

This is still not a workflow patch action.

## Reviewed Patch Target

The only future workflow hunk in scope is one new file:

- `.github/workflows/public-runtime-smoke.yml`

The reviewed patch may touch only:

- the new workflow file above
- comments or metadata inside that file
- read-only smoke-check steps inside that file

The reviewed patch must not touch:

- `.github/workflows/deploy-foundation-skeleton.yml`
- `app.py`
- any AWS planning JSON outside the future smoke workflow file
- any deploy workflow trigger or permission block

## Exact Patch Boundaries

The first reviewed patch must remain narrow enough that the repo still gains
no new deployment authority.

Allowed patch shape:

1. create only `.github/workflows/public-runtime-smoke.yml`
2. preserve `workflow_dispatch` as the only trigger
3. preserve workflow-level permissions as:
   - `contents: read`
4. preserve one job only:
   - `public-runtime-smoke`
5. derive `PUBLIC_BASE_URL` from `vars.FOUNDATION_PUBLIC_BASE_URL`
6. keep the workflow read-only and observational

The reviewed patch may describe and run future smoke behavior, but it must not
introduce deployment behavior.

## Allowed Patch Content

The first reviewed patch may contain only:

- workflow name and metadata for smoke checks
- `workflow_dispatch` inputs only if they remain non-secret and optional
- one job-local environment derivation for `PUBLIC_BASE_URL`
- shell using:
  - `curl`
  - `jq`
  - `sleep`
- a bounded three-round smoke loop with five-second spacing
- summary-only outcome reporting
- comments preserving read-only posture and non-secret boundary rules

The first reviewed patch must not contain:

- `schedule`
- `workflow_run`
- `push`
- `pull_request`
- `aws-actions/configure-aws-credentials`
- `aws` mutation commands
- `docker` commands
- rollback commands
- hardcoded live public base URLs

## Required Preserved Posture

Immediately before a later patch mission is allowed to start, these must still
be true:

- `app.py` has no new diff for this mission
- `.github/workflows/deploy-foundation-skeleton.yml` has no diff for this
  mission
- ECS service remains steady on the accepted runtime revision
- telemetry runtime identity remains aligned
- the stable ALB base URL remains non-secret and externally supplied
- secrets posture remains clean
- no schedule or chained trigger has been added elsewhere in source

## Review Outcomes

### 1. `smoke_automation_controlled_patch_blocked`

Required when:

- the reviewed diff touches any existing workflow file
- non-read-only behavior is introduced
- trigger widening is introduced
- AWS auth or mutation commands are introduced
- the live public base URL is hardcoded
- the Flask application contract is touched

### 2. `smoke_automation_controlled_patch_review_required`

Allowed when:

- the reviewed diff is narrow enough
- the future workflow stays separate from deployment authority
- the patch remains read-only
- operator review is still required before any patch mission

### 3. `smoke_automation_controlled_patch_ready_for_patch`

Allowed when:

- the reviewed diff is limited to one new workflow file
- the deploy workflow remains unchanged
- the workflow trigger remains `workflow_dispatch` only
- the smoke logic stays read-only and summary-only
- all preserved posture evidence still holds

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `smoke_automation_controlled_patch_ready_for_patch`, the following
remain forbidden in this mission:

- creating the workflow file
- modifying `.github/workflows/deploy-foundation-skeleton.yml`
- adding schedule or chained triggers
- adding AWS auth
- adding AWS mutation commands
- auto-rolling back on smoke failure
- bundling smoke automation with rollout or image-push logic

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/public-runtime-smoke-automation-controlled-patch-review.template.json`](./.github/public-runtime-smoke-automation-controlled-patch-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not a patch token.

## Source Boundary

Source may contain:

- reviewed patch scope
- preserved required lines
- blocked/review/ready outcomes
- explicit forbidden actions

Source must not contain:

- a created workflow file
- hardcoded live URLs
- credentials
- hidden trigger widening

## Governance Rules

- the controlled patch review must remain narrower than the proposal
- the controlled patch review must remain narrower than actual workflow
  mutation
- the deployment workflow must stay untouched
- the Flask service contract must remain untouched

## Explicit Non-Goals

This review does not:

- create the workflow file
- enable repeat scheduling
- create AWS trust
- create deployment automation
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_REVIEW_V1.md)
- [`.github/public-runtime-smoke-automation-controlled-patch-review.template.json`](./.github/public-runtime-smoke-automation-controlled-patch-review.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `GitHub-Hosted Public Runtime Smoke Workflow Dispatch Review v1`

That mission should decide whether the now-proven read-only smoke workflow is
ready for repository-backed hosted execution without widening triggers,
permissions, or deployment authority.
