# Dean'z Elite OS Public Verification Stage Enablement Proposal v1

## Purpose

This document defines the bounded proposal for how the
`public-verification-placeholder` job could be considered for a later
controlled patch without widening the push-image or rollout stages.

It exists to answer these questions after the public-verification candidate
review is complete:

- what is the exact minimal diff shape for a future public-verification patch?
- what must remain unchanged while that future patch is only being proposed?
- what evidence must be rechecked immediately before any controlled patch
  review is allowed?

This document does not:

- enable `public-verification-placeholder`
- run live public smoke tests
- commit production endpoint URLs
- mutate ALB, ECS, API Gateway, or DNS state
- change the Flask application contract

## Scope

This proposal applies only to:

- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact proposal shape for the third-job public-verification
boundary.

## Proposal Objective

The proposal exists to define whether `public-verification-placeholder` is:

- `public_verification_stage_proposal_blocked`
- `public_verification_stage_proposal_review_required`
- `public_verification_stage_proposal_ready_for_controlled_patch_review`

This is still not a patch or a public-verification enablement action.

## Minimal Diff Shape

The public-verification enablement proposal for
`public-verification-placeholder` must remain narrow.

Allowed proposed diff shape:

1. change only the `public-verification-placeholder` job
2. keep `push-image-placeholder` behavior unchanged
3. keep `ecs-rollout-placeholder` behavior unchanged
4. keep the workflow trigger as `workflow_dispatch` only
5. keep the workflow service-scoped to `task-planner-foundation`
6. keep workflow-level permissions at `contents: read`

Any proposal that widens beyond that is out of scope.

## Proposed Patch Boundaries

If a later controlled patch-review mission is attempted, the proposal should
allow only:

- re-evaluating the `if: ${{ false }}` gate for
  `public-verification-placeholder`
- one explicit verification-order comment block preserving the release-gate
  sequence
- one explicit future command shape for runtime verification of `/health`,
  `/status`, `/validate`, `/orchestrate`, and warning-bearing `/telemetry`
- reading approved non-secret routing inputs from repository or workflow
  variables rather than hardcoded source literals
- comments preserving bounded rollback posture and manual review outcomes

The proposal must not assume:

- push-image changes
- ECS rollout changes
- workflow-level permission widening
- committed production endpoint URLs
- automatic acceptance decisions

## Commands That Must Remain Proposal-Bound

Even in the proposed future patch shape, these commands remain proposal-only
until a later mission explicitly authorizes them:

- `curl`
- `wget`
- any equivalent public runtime probe command
- any command that mutates routing or deployment state
- any command that bypasses rollback or manual review posture

That means this mission may contain only:

- reviewed diff scope
- reviewed command ordering
- reviewed evidence and outcomes

not live public-verification workflow behavior.

## Recheck Evidence Before Any Controlled Patch Review

Immediately before a future controlled patch-review mission is allowed to
start, these must be rechecked:

- public-verification candidate review still allows
  `public-verification-placeholder`
- bounded ECR image publication run is still verifiable
- ECS service baseline is still steady
- `public-verification-placeholder` remains disabled
- `push-image-placeholder` remains unchanged
- `ecs-rollout-placeholder` remains unchanged
- `app.py` still has no diff
- release-gate posture is still present
- rollback posture is still explicit
- secrets posture is still clean

## Proposal Outcomes

### 1. `public_verification_stage_proposal_blocked`

Required when:

- the proposed diff touches more than `public-verification-placeholder`
- push-image or rollout behavior is changed
- workflow-level permissions widen
- live public verification is proposed without preserved release-gate posture
- committed endpoint URLs appear in source
- secrets posture is unsafe

### 2. `public_verification_stage_proposal_review_required`

Allowed when:

- the diff is narrow enough
- the job remains third in the sequence
- operator review is still required before any controlled patch review

### 3. `public_verification_stage_proposal_ready_for_controlled_patch_review`

Allowed when:

- the proposed diff is limited to the public-verification job
- `push-image-placeholder` behavior remains unchanged
- `ecs-rollout-placeholder` behavior remains unchanged
- future verification remains subordinate to the release-gate contract
- all recheck evidence remains satisfied

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `public_verification_stage_proposal_ready_for_controlled_patch_review`,
the following remain forbidden in this mission:

- modifying `push-image-placeholder`
- modifying `ecs-rollout-placeholder`
- enabling any job
- widening workflow-level permissions
- adding live public runtime checks to source
- committing production endpoint URLs
- bypassing release-gate or rollback posture

## Canonical Planning Artifact

The non-secret planning artifact for this proposal is:

- [`.github/public-verification-stage-enablement-proposal.template.json`](./.github/public-verification-stage-enablement-proposal.template.json)

That file is a planning artifact only.

It is not a patch and not a workflow control plane.

## Source Boundary

Source may contain:

- proposed diff scope
- recheck evidence
- blocked/review/proposal-ready outcomes
- explicit forbidden actions

Source must not contain:

- live public probe commands
- committed production endpoint URLs
- credentials
- hidden enablement flags

## Governance Rules

- the public-verification enablement proposal must remain downstream of the
  public-verification candidate review
- the proposal must remain narrower than actual public-verification job
  enablement
- push-image and rollout stages must remain unchanged
- application code must remain untouched

## Explicit Non-Goals

This proposal does not:

- patch the workflow
- enable a job
- create AWS credentials
- commit live runtime checks
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md)
- [`.github/public-verification-stage-enablement-proposal.template.json`](./.github/public-verification-stage-enablement-proposal.template.json)
- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [`.github/public-verification-stage-controlled-patch-review.template.json`](./.github/public-verification-stage-controlled-patch-review.template.json)

## Recommended Next Mission

The next bounded step after this proposal should be:

- `Public Verification Stage Controlled Patch Review v1`

That mission should inspect the exact workflow diff for only the third job and
confirm that it remains within the reviewed release-gate, rollback, and manual
review boundaries.
