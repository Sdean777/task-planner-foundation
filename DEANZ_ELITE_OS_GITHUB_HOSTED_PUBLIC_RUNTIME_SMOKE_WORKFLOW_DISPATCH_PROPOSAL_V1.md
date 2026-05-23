# Dean'z Elite OS GitHub-Hosted Public Runtime Smoke Workflow Dispatch Proposal v1

## Purpose

This document defines the bounded proposal for how the existing read-only
public runtime smoke workflow could later be executed through a repository-
backed GitHub-hosted dispatch for the `task-planner-foundation` service.

It exists to answer these questions after the hosted-dispatch review is
complete:

- what is the exact minimal future execution shape for a GitHub-hosted smoke
  dispatch?
- what must remain unchanged while that future hosted run is only being
  proposed?
- what evidence must be rechecked immediately before any controlled run review
  is allowed?

This proposal does not:

- run a GitHub-hosted workflow dispatch
- modify `.github/workflows/public-runtime-smoke.yml`
- modify `.github/workflows/deploy-foundation-skeleton.yml`
- add workflow inputs, triggers, or permissions
- change the Flask endpoint contract

## Scope

This proposal applies only to:

- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_RUNTIME_SMOKE_AUTOMATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_RUNTIME_SMOKE_AUTOMATION_RUN_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/workflows/public-runtime-smoke.yml`](./.github/workflows/public-runtime-smoke.yml)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)
- [`.github/github-hosted-public-runtime-smoke-workflow-dispatch-proposal.template.json`](./.github/github-hosted-public-runtime-smoke-workflow-dispatch-proposal.template.json)

It governs only the exact proposal shape for a later GitHub-hosted manual
dispatch of the existing read-only smoke workflow.

## Proposal Objective

The proposal exists to define whether hosted smoke dispatch is:

- `hosted_dispatch_proposal_blocked`
- `hosted_dispatch_proposal_review_required`
- `hosted_dispatch_proposal_ready_for_controlled_run_review`

This is still not a hosted workflow execution mission.

## Minimal Future Execution Shape

The future hosted-dispatch run must remain narrow.

Allowed proposed execution shape:

1. use the existing workflow file only:
   - `.github/workflows/public-runtime-smoke.yml`
2. keep `.github/workflows/public-runtime-smoke.yml` unchanged
3. keep `.github/workflows/deploy-foundation-skeleton.yml` unchanged
4. keep the workflow `workflow_dispatch` only
5. keep workflow-level permissions at `contents: read`
6. keep the run repository-backed and manual on `main`
7. keep the runtime input source at:
   - `vars.FOUNDATION_PUBLIC_BASE_URL`
8. keep the run service-scoped to `task-planner-foundation`
9. keep the hosted run read-only and observational

Any proposal that widens beyond that is out of scope.

## Proposed Hosted Dispatch Shape

If a later controlled run-review mission is attempted, the proposal should
allow only:

- workflow:
  - `Public Runtime Smoke`
- branch:
  - `main`
- runner:
  - `ubuntu-latest`
- job:
  - `public-runtime-smoke`
- runtime input source:
  - `vars.FOUNDATION_PUBLIC_BASE_URL`
- one derived runtime variable:
  - `PUBLIC_BASE_URL`
- one bounded three-round smoke loop with five-second spacing
- one read-only endpoint set:
  - `/`
  - `/health`
  - `/status`
  - `/tasks`
  - `/memory`
  - `/agent`
  - `/telemetry`
  - `/validate`
  - `/orchestrate`
- one summary-only workflow outcome
- one hosted-run evidence surface:
  - GitHub Actions run logs and step summary only

The proposal must not assume:

- any workflow source edit
- any extra workflow input
- any trigger widening
- any permission widening
- any AWS auth
- any ECS, ALB, or routing mutation
- any rollback authority

## Commands That Must Remain Proposal-Bound

Even in the proposed future hosted-dispatch shape, these remain proposal-only
until a later mission explicitly authorizes a controlled run review or bounded
hosted run:

- `gh workflow run`
- `gh run watch`
- `gh run view`
- any repository-variable mutation command
- any workflow-dispatch invocation through the GitHub UI

This mission may contain only:

- reviewed hosted-execution scope
- reviewed evidence and outcomes
- reviewed forbidden actions

not a real hosted dispatch.

## Recheck Evidence Before Any Controlled Run Review

Immediately before a future controlled run-review mission is allowed to start,
these must be rechecked:

- hosted-dispatch review still allows a later proposal-bound run
- `.github/workflows/public-runtime-smoke.yml` remains unchanged
- `.github/workflows/deploy-foundation-skeleton.yml` remains unchanged
- stable ALB base URL still exists
- runtime telemetry identity remains aligned
- the local-equivalent smoke automation evidence remains `stable`
- secrets posture remains clean
- no hidden trigger or permission widening has appeared in source

## Proposal Outcomes

### 1. `hosted_dispatch_proposal_blocked`

Required when:

- the proposal mutates either workflow file
- the proposal widens triggers or permissions
- the proposal adds AWS auth or mutation-bearing commands
- the proposal introduces workflow inputs, secrets, or variable mutation
- the proposal hardcodes the live public base URL

### 2. `hosted_dispatch_proposal_review_required`

Allowed when:

- the proposed execution shape is narrow enough
- the hosted run remains read-only
- operator review is still required before any controlled run review

### 3. `hosted_dispatch_proposal_ready_for_controlled_run_review`

Allowed when:

- the proposal uses the existing workflow file only
- both workflow files remain unchanged
- the hosted run remains `workflow_dispatch` only
- workflow-level permissions remain `contents: read`
- the runtime input remains the non-secret repository variable boundary
- all recheck evidence remains satisfied

This outcome still does not execute a hosted workflow run.

## Still-Forbidden Actions

Even after `hosted_dispatch_proposal_ready_for_controlled_run_review`, the
following remain forbidden in this mission:

- running the GitHub-hosted workflow dispatch
- modifying `.github/workflows/public-runtime-smoke.yml`
- modifying `.github/workflows/deploy-foundation-skeleton.yml`
- adding schedule, `workflow_run`, `push`, or `pull_request` triggers
- widening workflow permissions
- adding AWS auth or mutation commands
- hardcoding the live public base URL
- introducing rollback or remediation authority

## Canonical Planning Artifact

The non-secret planning artifact for this proposal is:

- [`.github/github-hosted-public-runtime-smoke-workflow-dispatch-proposal.template.json`](./.github/github-hosted-public-runtime-smoke-workflow-dispatch-proposal.template.json)

That file is a planning artifact only.

It is not a workflow run and not an approval token.

## Source Boundary

Source may contain:

- proposed hosted-execution scope
- proposed run shape
- recheck evidence
- blocked/review/proposal-ready outcomes
- explicit forbidden actions

Source must not contain:

- a real hosted workflow dispatch record
- workflow mutations in this mission
- credentials
- hidden trigger or permission widening

## Governance Rules

- hosted smoke dispatch must remain separate from deployment authority
- hosted smoke dispatch must remain read-only
- hosted smoke dispatch must remain narrower than deployment workflows
- hosted smoke dispatch outcomes must stay observational, not mutational
- both workflow files must remain unchanged in this proposal mission

## Explicit Non-Goals

This proposal does not:

- run the hosted workflow
- create a new workflow file
- modify deployment approvals
- create rollback behavior
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_RUNTIME_SMOKE_AUTOMATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_RUNTIME_SMOKE_AUTOMATION_RUN_V1.md)
- [`.github/github-hosted-public-runtime-smoke-workflow-dispatch-proposal.template.json`](./.github/github-hosted-public-runtime-smoke-workflow-dispatch-proposal.template.json)

## Recommended Next Mission

The next bounded step after this proposal should be:

- `GitHub-Hosted Public Runtime Smoke Workflow Dispatch Controlled Run Review v1`

That mission should inspect the exact repository-backed hosted-run boundary for
the existing read-only smoke workflow before any real GitHub-hosted dispatch
is attempted.
