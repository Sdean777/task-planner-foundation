# Dean'z Elite OS ECS Rollout Stage Enablement Proposal v1

## Purpose

This document defines the bounded proposal for how the
`ecs-rollout-placeholder` job could be considered for a later controlled patch
without advancing the public-verification stage.

It exists to answer these questions after the rollout-stage candidate review is
complete:

- what is the exact minimal diff shape for a future rollout-stage patch?
- what must remain unchanged while that future patch is only being proposed?
- what evidence must be rechecked immediately before any controlled patch
  review is allowed?

This document does not:

- enable `ecs-rollout-placeholder`
- register an ECS task definition
- update an ECS service
- enable `public-verification-placeholder`
- change the Flask application contract

## Scope

This proposal applies only to:

- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact proposal shape for the second-job rollout boundary.

## Proposal Objective

The proposal exists to define whether `ecs-rollout-placeholder` is:

- `rollout_stage_proposal_blocked`
- `rollout_stage_proposal_review_required`
- `rollout_stage_proposal_ready_for_controlled_patch_review`

This is still not a patch or a rollout-enable action.

## Minimal Diff Shape

The rollout-stage enablement proposal for `ecs-rollout-placeholder` must remain
narrow.

Allowed proposed diff shape:

1. change only the `ecs-rollout-placeholder` job
2. keep `push-image-placeholder` behavior unchanged
3. keep `public-verification-placeholder` disabled
4. keep the workflow trigger as `workflow_dispatch` only
5. keep the workflow service-scoped to `task-planner-foundation`
6. keep workflow-level permissions at `contents: read`

Any proposal that widens beyond that is out of scope.

## Proposed Patch Boundaries

If a later controlled patch-review mission is attempted, the proposal should
allow only:

- re-evaluating the `if: ${{ false }}` gate for `ecs-rollout-placeholder`
- reading previously published immutable image input from approved non-secret
  workflow or repository variables
- one explicit task-definition registration command shape referencing immutable
  `sha-<git-sha>` image truth
- one explicit ECS service update command shape referencing a single new task
  definition revision
- comments preserving `public-verification-placeholder` disablement

The proposal must not assume:

- public verification changes
- application-code changes
- workflow-level permission widening
- mutable tag truth without immutable SHA linkage

## Commands That Must Remain Proposal-Bound

Even in the proposed future patch shape, these commands remain proposal-only
until a later mission explicitly authorizes them:

- `aws ecs register-task-definition`
- `aws ecs update-service`
- any command that bypasses the recorded previous known-good revision
- any command that advances `public-verification-placeholder`

That means this mission may contain only:

- reviewed diff scope
- reviewed command ordering
- reviewed evidence and outcomes

not live ECS-mutating workflow behavior.

## Recheck Evidence Before Any Controlled Patch Review

Immediately before a future controlled patch-review mission is allowed to
start, these must be rechecked:

- rollout-stage candidate review still allows `ecs-rollout-placeholder`
- first bounded ECR image publication run is still verifiable
- immutable SHA image truth is still present in ECR
- `main` still resolves to the same published digest
- `app.py` still has no diff
- `push-image-placeholder` remains the only live-capable job
- `public-verification-placeholder` remains disabled
- rollout contract still requires explicit revision handoff and rollback
- release-gate posture is still present
- secrets posture is still clean

## Proposal Outcomes

### 1. `rollout_stage_proposal_blocked`

Required when:

- the proposed diff touches more than `ecs-rollout-placeholder`
- `public-verification-placeholder` changes
- workflow-level permissions widen
- live ECS mutation is proposed without preserved boundaries
- immutable image truth or rollback posture drifts
- secrets posture is unsafe

### 2. `rollout_stage_proposal_review_required`

Allowed when:

- the diff is narrow enough
- the job remains second in the sequence
- operator review is still required before any controlled patch review

### 3. `rollout_stage_proposal_ready_for_controlled_patch_review`

Allowed when:

- the proposed diff is limited to the rollout job
- `push-image-placeholder` behavior remains unchanged
- `public-verification-placeholder` remains disabled
- rollout identity remains subordinate to immutable SHA image truth
- all recheck evidence remains satisfied

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `rollout_stage_proposal_ready_for_controlled_patch_review`, the
following remain forbidden in this mission:

- modifying `push-image-placeholder`
- modifying `public-verification-placeholder`
- enabling any job
- widening workflow-level permissions
- adding live AWS-mutating behavior to source
- bypassing immutable tag, rollback, or release-gate posture

## Canonical Planning Artifact

The non-secret planning artifact for this proposal is:

- [`.github/ecs-rollout-stage-enablement-proposal.template.json`](./.github/ecs-rollout-stage-enablement-proposal.template.json)

That file is a planning artifact only.

It is not a patch and not a workflow control plane.

## Source Boundary

Source may contain:

- proposed diff scope
- recheck evidence
- blocked/review/proposal-ready outcomes
- explicit forbidden actions

Source must not contain:

- live task-definition registration
- live ECS service updates
- credentials
- hidden enablement flags

## Governance Rules

- the rollout-stage enablement proposal must remain downstream of the rollout-stage candidate review
- the proposal must remain narrower than actual rollout-job enablement
- `public-verification-placeholder` must stay blocked
- application code must remain untouched

## Explicit Non-Goals

This proposal does not:

- patch the workflow
- enable a job
- create AWS credentials
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md)
- [`.github/ecs-rollout-stage-enablement-proposal.template.json`](./.github/ecs-rollout-stage-enablement-proposal.template.json)
- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [`.github/ecs-rollout-stage-controlled-patch-review.template.json`](./.github/ecs-rollout-stage-controlled-patch-review.template.json)

## Recommended Next Mission

The next bounded step after this proposal should be:

- `ECS Rollout Stage Controlled Patch Review v1`

That mission should inspect the exact workflow diff for only the second job and
confirm that it remains within the reviewed immutability, rollback, and
release-gate boundaries before any patch is applied.

## Warning

Do not treat this proposal as permission to mutate ECS.

It only defines the exact narrow shape a later controlled patch-review mission
must obey.
