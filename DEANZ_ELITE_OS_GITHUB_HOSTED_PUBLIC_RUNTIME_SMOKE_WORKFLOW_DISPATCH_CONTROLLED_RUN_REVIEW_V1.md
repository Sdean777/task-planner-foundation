# Dean'z Elite OS GitHub-Hosted Public Runtime Smoke Workflow Dispatch Controlled Run Review v1

## Purpose

This document defines the first bounded controlled-run review for the existing
read-only public runtime smoke workflow for the `task-planner-foundation`
service.

It exists to answer these questions before any real GitHub-hosted dispatch is
attempted:

- what exact hosted run boundary is reviewable?
- what workflow lines, triggers, permissions, and runtime inputs must remain
  unchanged around that run?
- what evidence must still be rechecked immediately before a first bounded
  hosted dispatch?
- how does the reviewed run remain read-only and separate from deployment
  authority?

This review does not:

- run a GitHub-hosted workflow dispatch
- modify `.github/workflows/public-runtime-smoke.yml`
- modify `.github/workflows/deploy-foundation-skeleton.yml`
- add workflow inputs, triggers, or permissions
- change the Flask application contract

## Scope

This controlled-run review applies to:

- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_PROPOSAL_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_RUNTIME_SMOKE_AUTOMATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_RUNTIME_SMOKE_AUTOMATION_RUN_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/workflows/public-runtime-smoke.yml`](./.github/workflows/public-runtime-smoke.yml)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)
- [`.github/github-hosted-public-runtime-smoke-workflow-dispatch-controlled-run-review.template.json`](./.github/github-hosted-public-runtime-smoke-workflow-dispatch-controlled-run-review.template.json)

It governs only the exact review boundary for one future repository-backed
GitHub-hosted dispatch of the existing smoke workflow.

## Controlled Run Review Objective

This review exists to decide whether the future hosted smoke dispatch remains:

- `hosted_dispatch_controlled_run_blocked`
- `hosted_dispatch_controlled_run_review_required`
- `hosted_dispatch_ready_for_first_bounded_run`

This is still not a hosted workflow execution action.

## Reviewed Run Target

The only future hosted run in scope is one dispatch of:

- `.github/workflows/public-runtime-smoke.yml`

The reviewed run may rely only on:

- repository branch `main`
- trigger `workflow_dispatch`
- workflow-level permissions:
  - `contents: read`
- runtime input source:
  - `vars.FOUNDATION_PUBLIC_BASE_URL`
- one existing job:
  - `public-runtime-smoke`

The reviewed run must not require:

- workflow source edits
- deploy workflow edits
- extra workflow inputs
- variable mutation
- approval bypass
- any AWS mutation or auth step

## Exact Run Boundaries

The first reviewed hosted dispatch must remain narrow enough that the repo
still gains no new deployment authority.

Allowed run shape:

1. dispatch only `.github/workflows/public-runtime-smoke.yml`
2. dispatch on `main` only
3. keep the workflow file unchanged
4. keep `.github/workflows/deploy-foundation-skeleton.yml` unchanged
5. keep workflow-level permissions at:
   - `contents: read`
6. preserve one existing job only:
   - `public-runtime-smoke`
7. preserve `vars.FOUNDATION_PUBLIC_BASE_URL` as the only runtime input source
8. preserve read-only endpoint verification only
9. preserve GitHub Actions logs and step summary as the only hosted evidence
   surfaces

The reviewed run may execute the already-reviewed smoke behavior, but it must
not introduce deployment behavior.

## Allowed Hosted Run Content

The first reviewed hosted run may contain and use only:

- the existing workflow name and metadata
- `workflow_dispatch` with no new inputs
- the existing `PUBLIC_BASE_URL` derivation
- the existing three-round smoke loop
- the existing read-only endpoint set:
  - `/`
  - `/health`
  - `/status`
  - `/tasks`
  - `/memory`
  - `/agent`
  - `/telemetry`
  - `/validate`
  - `/orchestrate`
- the existing summary-only outcome reporting
- hosted evidence collected from:
  - Actions run logs
  - step summary

The first reviewed hosted run must not contain or require:

- `schedule`
- `workflow_run`
- `push`
- `pull_request`
- workflow-file mutation
- deploy-workflow mutation
- `aws-actions/configure-aws-credentials`
- `aws` mutation commands
- `docker` commands
- rollback commands
- hardcoded live public base URLs

## Required Preserved Posture

Immediately before a later bounded run mission is allowed to start, these must
still be true:

- `app.py` has no new diff for this mission
- `.github/workflows/public-runtime-smoke.yml` has no diff for this mission
- `.github/workflows/deploy-foundation-skeleton.yml` has no diff for this
  mission
- the stable ALB base URL remains non-secret and externally supplied
- ECS service remains steady on the accepted runtime revision
- telemetry runtime identity remains aligned
- the local-equivalent smoke automation evidence remains `stable`
- secrets posture remains clean
- no trigger or permission widening has appeared elsewhere in source

## Review Outcomes

### 1. `hosted_dispatch_controlled_run_blocked`

Required when:

- the reviewed run needs workflow-file mutation
- the reviewed run needs deploy-workflow mutation
- trigger or permission widening is introduced
- extra inputs or variable mutation are introduced
- AWS auth or mutation commands are introduced
- the live public base URL is hardcoded
- the Flask application contract is touched

### 2. `hosted_dispatch_controlled_run_review_required`

Allowed when:

- the reviewed run is narrow enough
- the future dispatch stays separate from deployment authority
- the hosted run remains read-only
- operator review is still required before any bounded run mission

### 3. `hosted_dispatch_ready_for_first_bounded_run`

Allowed when:

- the reviewed run is limited to the existing workflow file only
- both workflow files remain unchanged
- the workflow trigger remains `workflow_dispatch` only
- workflow-level permissions remain `contents: read`
- the runtime input remains the non-secret repository variable boundary
- the smoke logic stays read-only and summary-only
- all preserved posture evidence still holds

This outcome still does not execute a hosted run.

## Still-Forbidden Actions

Even after `hosted_dispatch_ready_for_first_bounded_run`, the following remain
forbidden in this mission:

- running the GitHub-hosted workflow dispatch
- modifying `.github/workflows/public-runtime-smoke.yml`
- modifying `.github/workflows/deploy-foundation-skeleton.yml`
- adding schedule or chained triggers
- widening workflow permissions
- adding AWS auth
- adding AWS mutation commands
- hardcoding the live public base URL
- auto-rolling back on smoke failure

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/github-hosted-public-runtime-smoke-workflow-dispatch-controlled-run-review.template.json`](./.github/github-hosted-public-runtime-smoke-workflow-dispatch-controlled-run-review.template.json)

That file is a planning artifact only.

It is not a hosted workflow control plane and not a run token.

## Source Boundary

Source may contain:

- reviewed run scope
- preserved required lines and boundaries
- blocked/review/ready outcomes
- explicit forbidden actions

Source must not contain:

- a hosted workflow run record
- workflow mutations in this mission
- credentials
- hidden trigger or permission widening

## Governance Rules

- the controlled run review must remain narrower than the proposal
- the controlled run review must remain narrower than an actual hosted run
- both workflow files must stay untouched
- the Flask service contract must stay untouched
- hosted smoke dispatch must remain read-only and observational

## Explicit Non-Goals

This review does not:

- run the hosted workflow
- mutate workflow files
- create AWS trust
- create deployment automation
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_PROPOSAL_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_REVIEW_V1.md)
- [`.github/github-hosted-public-runtime-smoke-workflow-dispatch-controlled-run-review.template.json`](./.github/github-hosted-public-runtime-smoke-workflow-dispatch-controlled-run-review.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `First Bounded GitHub-Hosted Public Runtime Smoke Workflow Dispatch Run v1`

That mission should execute one repository-backed hosted dispatch of the
existing read-only smoke workflow without widening triggers, permissions, or
deployment authority.
