# Dean'z Elite OS Public Runtime Smoke Automation Review v1

## Purpose

This document defines the first bounded review layer for automating the now-
proven post-deploy public runtime smoke checks for the
`task-planner-foundation` service.

It exists to answer these questions:

- is there now enough stable evidence to review a future smoke-automation
  layer?
- what exact smoke evidence may be automated later without widening
  deployment authority?
- which automation shapes remain forbidden even after the first clean
  `keep_active` release result?

This review does not:

- create a smoke workflow
- modify the deployment workflow
- rerun deployment, rollout, or routing changes
- add AWS credentials to source
- change the Flask endpoint contract

## Scope

This review applies to:

- [DEANZ_ELITE_OS_POST_DEPLOY_PUBLIC_RUNTIME_SMOKE_TESTS_V1.md](./DEANZ_ELITE_OS_POST_DEPLOY_PUBLIC_RUNTIME_SMOKE_TESTS_V1.md)
- [DEANZ_ELITE_OS_TELEMETRY_RUNTIME_IDENTITY_ALIGNMENT_V1.md](./DEANZ_ELITE_OS_TELEMETRY_RUNTIME_IDENTITY_ALIGNMENT_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)
- [`.github/public-runtime-smoke-automation-review.template.json`](./.github/public-runtime-smoke-automation-review.template.json)

It governs only the review boundary for a future read-only smoke-automation
layer.

## Review Objective

This review exists to decide whether public runtime smoke automation currently
remains:

- `smoke_automation_blocked`
- `smoke_automation_review_required`
- `smoke_automation_candidate_ready`

This is still not an automation implementation mission.

## Required Evidence

Before any future smoke-automation proposal may reopen, the following must
already exist and remain intact.

### 1. Foundation Preservation

- [app.py](./app.py) remains the bounded foundation service
- the current Flask endpoint contract remains intact
- the deployment workflow skeleton still exists
- the public-verification workflow job remains the deployment-time release
  gate, not a general smoke-automation engine

### 2. Stable Runtime Truth

- the ECS service rollout is complete on `task-planner-foundation:2`
- the stable ALB base URL exists
- the second bounded public verification run completed honestly
- telemetry runtime identity alignment completed
- the post-deploy public runtime smoke tests completed with:
  - three passing rounds
  - no endpoint drift
  - no runtime-identity regression
  - no new warning-bearing condition

### 3. Automation Boundary Preservation

- any future smoke automation must remain downstream of `keep_active`
- any future smoke automation must stay read-only
- any future smoke automation must not mutate:
  - ECR
  - ECS
  - ALB
  - target groups
  - DNS
  - API Gateway
- any future smoke automation must not create rollback authority
- any future smoke automation must not become a hidden deployment controller

### 4. Future Allowed Signal Classes

If a later automation layer is proposed, it may only automate evidence already
proven in the manual smoke pass:

- public root response
- `/health`
- `/status`
- `/tasks`
- `/memory`
- `/agent`
- `/telemetry`
- `/validate`
- `/orchestrate`
- optional read-only ECS service state inspection
- optional read-only target-health inspection
- optional read-only CloudWatch log-stream visibility

### 5. Source Hygiene

- no AWS credentials in source
- no OpenAI or model keys in source
- no hardcoded public base URL in workflow source
- no hidden automation triggers in source
- no bundling of smoke automation with image publication or rollout logic

## Candidate Constraints

Even if smoke automation becomes a candidate, the following must remain true
in this mission:

- no new workflow file is created
- `.github/workflows/deploy-foundation-skeleton.yml` remains unchanged
- no schedule trigger is introduced
- no `workflow_run` chaining is introduced
- no automatic post-deploy execution path is introduced
- no approval bypass is introduced
- no smoke failure may auto-roll back infrastructure

## Review Outcomes

### 1. `smoke_automation_blocked`

Required when:

- stable public smoke evidence is missing
- telemetry alignment is incomplete
- smoke automation is proposed as a deployment or rollback controller
- mutation-bearing AWS commands are proposed
- workflow-trigger widening is proposed too early

### 2. `smoke_automation_review_required`

Allowed when:

- stable public smoke evidence exists
- release posture is already `keep_active`
- a later automation shape still needs exact boundary definition
- the future surface is not yet narrowed enough for a patch proposal

### 3. `smoke_automation_candidate_ready`

Allowed when:

- the stable ALB smoke evidence is complete
- automation scope is explicitly read-only
- the future automation layer remains separate from rollout authority
- the future automation surface is limited to proven smoke checks only
- source hygiene and non-secret boundary discipline remain intact

This outcome only allows a later proposal mission. It does not authorize any
automation patch by itself.

## Still-Forbidden Actions

Even after `smoke_automation_candidate_ready`, the following remain forbidden
in this mission:

- creating a new smoke workflow
- changing the deploy workflow
- adding `schedule`, `push`, `pull_request`, or `workflow_run` triggers
- hardcoding the live public base URL into workflow source
- adding AWS auth for mutation-bearing commands
- auto-rolling back on smoke failure
- combining smoke automation with image push or ECS rollout logic

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/public-runtime-smoke-automation-review.template.json`](./.github/public-runtime-smoke-automation-review.template.json)

That file is a planning artifact only.

It is not a workflow and not an approval token.

## Governance Rules

- smoke automation must remain downstream of release acceptance
- smoke automation must remain narrower than deployment automation
- smoke automation must stay read-only
- smoke automation outcomes must remain observational, not mutational
- smoke automation must not silently widen infrastructure authority

## Explicit Non-Goals

This review does not:

- create a smoke automation workflow
- add repeat cron checks
- modify deployment approvals
- create rollback logic
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_POST_DEPLOY_PUBLIC_RUNTIME_SMOKE_TESTS_V1.md](./DEANZ_ELITE_OS_POST_DEPLOY_PUBLIC_RUNTIME_SMOKE_TESTS_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/public-runtime-smoke-automation-review.template.json`](./.github/public-runtime-smoke-automation-review.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `GitHub-Hosted Public Runtime Smoke Workflow Dispatch Review v1`

That mission should decide whether the now-proven read-only smoke workflow is
ready for repository-backed hosted execution without widening triggers,
permissions, or deployment authority.
