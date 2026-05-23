# Dean'z Elite OS Public Verification Stage Controlled Patch Review v1

## Purpose

This document defines the bounded controlled-patch review for the
`public-verification-placeholder` job inside the `task-planner-foundation`
deployment workflow skeleton.

It exists to answer these questions before any future public-verification patch
is considered:

- what exact workflow hunk is reviewable for a future public-verification
  attempt?
- what lines must remain unchanged inside that hunk?
- what evidence must still be rechecked immediately before any later patch?
- how does the reviewed patch remain third-job-only and bounded by release-gate
  order, rollback posture, and manual review outcomes?

This document does not:

- patch the workflow
- enable `public-verification-placeholder`
- run live public smoke tests
- commit production endpoint URLs
- mutate ALB, ECS, API Gateway, or DNS state
- change the Flask application contract

## Scope

This controlled-patch review applies to:

- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact third-job public-verification patch-review boundary.

## Controlled Patch Review Objective

This review exists to decide whether the reviewed third workflow patch remains:

- `public_verification_stage_controlled_patch_blocked`
- `public_verification_stage_controlled_patch_review_required`
- `public_verification_stage_controlled_patch_ready_for_patch_mission`

This is still not a workflow patch action.

## Reviewed Patch Target

The only workflow hunk in scope is the `public-verification-placeholder` job.

The reviewed patch may touch only:

- the `if: ${{ false }}` gate for that job
- comments directly above that job
- job-local step ordering inside that job
- job-local lines required to preserve release-gate order, rollback posture,
  warning-bearing telemetry posture, and manual review outcomes

The reviewed patch must not touch:

- `push-image-placeholder`
- `ecs-rollout-placeholder`
- workflow trigger shape
- workflow service scope
- workflow-level permissions

## Exact Patch Boundaries

The reviewed public-verification patch must remain narrow enough that release
discipline stays visible and auditable.

Allowed reviewed patch shape:

1. change only the `public-verification-placeholder` job
2. preserve `needs: ecs-rollout-placeholder`
3. preserve the job name `public-verification-placeholder`
4. preserve `workflow_dispatch` as the only trigger
5. preserve workflow-level `permissions: contents: read`
6. preserve `push-image-placeholder` and `ecs-rollout-placeholder` unchanged
7. keep release outcomes limited to `keep_active`,
   `manual_review_required`, and `rollback_required`
8. keep public verification subordinate to rollback and previous known-good
   runtime identity

The reviewed patch may describe or position future third-job behavior, but it
must not widen beyond the public-verification job.

## Allowed Reviewed Patch Content

The reviewed patch may contain only:

- a re-evaluated third-job `if:` gate for `public-verification-placeholder`
- reading approved non-secret routing and runtime inputs from repository or
  workflow variables
- one explicit public verification command shape for `/health`
- one explicit public verification command shape for `/status`
- one explicit public verification command shape for `/validate`
- one explicit public verification command shape for `/orchestrate`
- one warning-bearing command shape for `/telemetry`
- clarifying comments or ordering that preserve rollback-required and
  manual-review outcomes

The reviewed patch must not contain:

- any change to workflow-level permissions
- any change to `push-image-placeholder`
- any change to `ecs-rollout-placeholder`
- any hardcoded production endpoint URL
- any application-code change
- any static AWS credential
- any hidden enablement flag outside `public-verification-placeholder`

## Required Preserved Posture

Immediately before a later public-verification patch mission is allowed to
start, these must still be true:

- `app.py` has no diff
- bounded ECR image publication remains verifiable
- ECS service baseline remains steady
- `push-image-placeholder` behavior remains unchanged
- `ecs-rollout-placeholder` behavior remains unchanged
- release-gate contract still requires ordered verification and bounded
  decision classes
- rollback posture remains explicit
- workflow-level permissions remain `contents: read`
- secrets posture remains clean
- no production endpoint URLs are committed in source

## Review Outcomes

### 1. `public_verification_stage_controlled_patch_blocked`

Required when:

- the reviewed diff touches any job beyond `public-verification-placeholder`
- workflow-level permissions are widened
- production endpoint URLs are committed into source
- live public verification bypasses release-gate order or rollback posture
- the Flask application contract is touched

### 2. `public_verification_stage_controlled_patch_review_required`

Allowed when:

- the reviewed diff is narrow enough
- the patch remains third-job-only
- release-gate order, rollback posture, and manual review outcomes remain
  explicit
- operator review is still required before any patch mission

### 3. `public_verification_stage_controlled_patch_ready_for_patch_mission`

Allowed when:

- the reviewed diff is limited to the public-verification job hunk
- `push-image-placeholder` remains unchanged
- `ecs-rollout-placeholder` remains unchanged
- workflow-level permissions remain unchanged
- all preserved posture evidence still holds
- the patch remains bounded by the reviewed release-gate chain

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `public_verification_stage_controlled_patch_ready_for_patch_mission`,
the following remain forbidden in this mission:

- modifying `push-image-placeholder`
- modifying `ecs-rollout-placeholder`
- widening workflow-level permissions
- committing production endpoint URLs
- bypassing release-gate order, rollback posture, or manual review outcomes
- changing `app.py`
- introducing static AWS credentials

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/public-verification-stage-controlled-patch-review.template.json`](./.github/public-verification-stage-controlled-patch-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not a patch token.

## Source Boundary

Source may contain:

- reviewed patch scope
- preserved required lines
- blocked/review/ready outcomes
- explicit forbidden actions

Source must not contain:

- live public probe commands outside the reviewed third-job boundary
- credentials
- hidden enablement flags
- a patched workflow body in this mission

## Governance Rules

- the public-verification controlled patch review must remain downstream of the
  public-verification proposal
- the public-verification controlled patch review must remain narrower than
  actual job enablement
- push-image and rollout jobs must stay unchanged
- the Flask service contract must remain untouched

## Explicit Non-Goals

This review does not:

- patch the workflow
- enable any job
- create AWS trust
- create routing infrastructure
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md)
- [`.github/public-verification-stage-controlled-patch-review.template.json`](./.github/public-verification-stage-controlled-patch-review.template.json)
- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_PATCH_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_PATCH_V1.md)
- [`.github/public-verification-stage-patch.template.json`](./.github/public-verification-stage-patch.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `Public Verification Stage Patch v1`

That mission should patch only the already-reviewed third-job path while
preserving push-image behavior, rollout behavior, release-gate order, rollback
posture, and manual review discipline.

## Warning

Do not treat this review as permission to patch the workflow freely.
