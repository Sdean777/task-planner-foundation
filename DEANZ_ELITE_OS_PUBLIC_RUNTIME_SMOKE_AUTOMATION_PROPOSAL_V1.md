# Dean'z Elite OS Public Runtime Smoke Automation Proposal v1

## Purpose

This document defines the bounded proposal for how a future read-only public
runtime smoke-automation layer could be added for the
`task-planner-foundation` service without widening deployment authority.

It exists to answer these questions after the smoke-automation review is
complete:

- what is the exact minimal future diff shape for smoke automation?
- what must remain unchanged while that future patch is only being proposed?
- what evidence must be rechecked immediately before any controlled patch
  review is allowed?

This proposal does not:

- create a workflow
- modify the deployment workflow
- add a schedule trigger
- rerun rollout or routing changes
- change the Flask endpoint contract

## Scope

This proposal applies only to:

- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_REVIEW_V1.md)
- [DEANZ_ELITE_OS_POST_DEPLOY_PUBLIC_RUNTIME_SMOKE_TESTS_V1.md](./DEANZ_ELITE_OS_POST_DEPLOY_PUBLIC_RUNTIME_SMOKE_TESTS_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)
- [`.github/public-runtime-smoke-automation-proposal.template.json`](./.github/public-runtime-smoke-automation-proposal.template.json)

It governs only the exact proposal shape for a later read-only smoke
automation boundary.

## Proposal Objective

The proposal exists to define whether smoke automation is:

- `smoke_automation_proposal_blocked`
- `smoke_automation_proposal_review_required`
- `smoke_automation_proposal_ready_for_controlled_patch_review`

This is still not a patch or a workflow implementation mission.

## Minimal Future Diff Shape

The future smoke-automation patch must remain narrow.

Allowed proposed diff shape:

1. add one new workflow file only:
   - `.github/workflows/public-runtime-smoke.yml`
2. keep `.github/workflows/deploy-foundation-skeleton.yml` unchanged
3. keep the future smoke workflow `workflow_dispatch` only
4. keep workflow-level permissions at `contents: read`
5. keep the workflow service-scoped to `task-planner-foundation`
6. keep the workflow read-only and observational

Any proposal that widens beyond that is out of scope.

## Proposed Future Workflow Shape

If a later controlled patch-review mission is attempted, the proposal should
allow only:

- one workflow named for public runtime smoke checks
- one single job, for example:
  - `public-runtime-smoke`
- one non-secret input source:
  - repository variable `FOUNDATION_PUBLIC_BASE_URL`
- one derived runtime variable:
  - `PUBLIC_BASE_URL` stripped of a trailing slash
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
- one summary-only outcome written to the workflow step summary

The proposal must not assume:

- schedule triggers
- `workflow_run` chaining
- push triggers
- pull-request triggers
- AWS auth
- ECS mutation
- rollback authority

## Commands That Must Remain Proposal-Bound

Even in the proposed future patch shape, these commands remain proposal-only
until a later mission explicitly authorizes them:

- `curl`
- `jq`
- shell loops for repeated smoke rounds
- any optional read-only AWS inspection command

This mission may contain only:

- reviewed diff scope
- reviewed command ordering
- reviewed evidence and outcomes

not a real workflow implementation.

## Recheck Evidence Before Any Controlled Patch Review

Immediately before a future controlled patch-review mission is allowed to
start, these must be rechecked:

- smoke-automation review still allows a later proposal-bound patch
- stable ALB base URL still exists
- ECS service revision `:2` or later is still steady
- telemetry runtime identity remains aligned
- post-deploy smoke evidence remains clean
- deploy workflow remains unchanged
- secrets posture remains clean
- no hidden trigger widening has appeared in source

## Proposal Outcomes

### 1. `smoke_automation_proposal_blocked`

Required when:

- the proposal mutates the deploy workflow
- the proposal adds schedule or workflow-run chaining
- the proposal introduces AWS mutation commands
- the proposal hardcodes the live public base URL
- the proposal widens beyond one new read-only workflow file

### 2. `smoke_automation_proposal_review_required`

Allowed when:

- the proposed diff is narrow enough
- the future workflow remains read-only
- operator review is still required before any controlled patch review

### 3. `smoke_automation_proposal_ready_for_controlled_patch_review`

Allowed when:

- the proposal is limited to one new read-only workflow file
- the deploy workflow remains unchanged
- the future workflow remains `workflow_dispatch` only
- the future signal set is limited to the proven smoke checks
- all recheck evidence remains satisfied

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after
`smoke_automation_proposal_ready_for_controlled_patch_review`, the following
remain forbidden in this mission:

- creating the workflow file
- modifying the deployment workflow
- adding schedule or workflow-run triggers
- hardcoding the live public base URL in source
- introducing AWS auth or mutation commands
- auto-rolling back on smoke failure
- combining smoke automation with rollout or image-push logic

## Canonical Planning Artifact

The non-secret planning artifact for this proposal is:

- [`.github/public-runtime-smoke-automation-proposal.template.json`](./.github/public-runtime-smoke-automation-proposal.template.json)

That file is a planning artifact only.

It is not a workflow and not an approval token.

## Source Boundary

Source may contain:

- proposed diff scope
- proposed workflow shape
- recheck evidence
- blocked/review/proposal-ready outcomes
- explicit forbidden actions

Source must not contain:

- a real smoke workflow
- hardcoded live public URLs
- credentials
- hidden automation triggers

## Governance Rules

- smoke automation must remain separate from deployment authority
- smoke automation must remain read-only
- smoke automation must remain narrower than release-gate automation
- smoke automation outcomes must stay observational, not mutational
- the deploy workflow must remain unchanged in this proposal mission

## Explicit Non-Goals

This proposal does not:

- create the workflow file
- enable repeat cron checks
- modify deployment approvals
- create rollback behavior
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_REVIEW_V1.md)
- [DEANZ_ELITE_OS_POST_DEPLOY_PUBLIC_RUNTIME_SMOKE_TESTS_V1.md](./DEANZ_ELITE_OS_POST_DEPLOY_PUBLIC_RUNTIME_SMOKE_TESTS_V1.md)
- [`.github/public-runtime-smoke-automation-proposal.template.json`](./.github/public-runtime-smoke-automation-proposal.template.json)

## Recommended Next Mission

The next bounded step after this proposal should be:

- `GitHub-Hosted Public Runtime Smoke Workflow Dispatch Review v1`

That mission should decide whether the now-proven read-only smoke workflow is
ready for repository-backed hosted execution without widening triggers,
permissions, or deployment authority.
