# Dean'z Elite OS ECS Rollout Stage Controlled Patch Review v1

## Purpose

This document defines the bounded controlled-patch review for the
`ecs-rollout-placeholder` job inside the `task-planner-foundation`
deployment workflow skeleton.

It exists to answer these questions before any future rollout-stage patch is
considered:

- what exact workflow hunk is reviewable for a future rollout-stage attempt?
- what lines must remain unchanged inside that hunk?
- what evidence must still be rechecked immediately before any later patch?
- how does the reviewed patch remain second-job-only and bounded by immutable
  image truth, rollback posture, and release-gate posture?

This document does not:

- patch the workflow
- enable `ecs-rollout-placeholder`
- register an ECS task definition
- update an ECS service
- change the Flask application contract

## Scope

This controlled-patch review applies to:

- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact second-job rollout patch-review boundary.

## Controlled Patch Review Objective

This review exists to decide whether the reviewed second workflow patch
remains:

- `rollout_stage_controlled_patch_blocked`
- `rollout_stage_controlled_patch_review_required`
- `rollout_stage_controlled_patch_ready_for_patch_mission`

This is still not a workflow patch action.

## Reviewed Patch Target

The only workflow hunk in scope is the `ecs-rollout-placeholder` job.

The reviewed patch may touch only:

- the `if: ${{ false }}` gate for that job
- comments directly above that job
- job-local step ordering inside that job
- job-local lines required to preserve immutable image input, explicit
  task-definition revision handoff, rollback posture, and public-verification
  disablement

The reviewed patch must not touch:

- `push-image-placeholder`
- `public-verification-placeholder`
- workflow trigger shape
- workflow service scope
- workflow-level permissions

## Exact Patch Boundaries

The reviewed rollout patch must remain narrow enough that rollout discipline
stays visible and auditable.

Allowed reviewed patch shape:

1. change only the `ecs-rollout-placeholder` job
2. preserve `needs: push-image-placeholder`
3. preserve the job name `ecs-rollout-placeholder`
4. preserve `workflow_dispatch` as the only trigger
5. preserve workflow-level `permissions: contents: read`
6. preserve `public-verification-placeholder` as disabled and unchanged
7. keep rollout identity subordinate to immutable `sha-<git-sha>` image truth
8. keep rollback identity subordinate to the previous known-good revision

The reviewed patch may describe or position future second-job behavior, but it
must not widen beyond the rollout job.

## Allowed Reviewed Patch Content

The reviewed patch may contain only:

- a re-evaluated second-job `if:` gate for `ecs-rollout-placeholder`
- reading approved non-secret image, cluster, service, and task-family inputs
- one explicit `aws ecs register-task-definition` command shape subordinate to
  immutable image truth
- one explicit `aws ecs update-service` command shape subordinate to the new
  revision and previous known-good rollback posture
- clarifying comments or ordering that preserve `public-verification-placeholder`
  disablement and release-gate posture

The reviewed patch must not contain:

- any change to workflow-level permissions
- any change to `push-image-placeholder`
- any change to `public-verification-placeholder`
- any public verification command
- any application-code change
- any static AWS credential
- any hidden enablement flag outside `ecs-rollout-placeholder`

## Required Preserved Posture

Immediately before a later rollout-stage patch mission is allowed to start,
these must still be true:

- `app.py` has no diff
- the first bounded ECR image publication run remains verifiable
- immutable SHA image truth remains present in ECR
- `main` still resolves to the same published digest
- `push-image-placeholder` behavior remains unchanged
- `public-verification-placeholder` remains disabled and unchanged
- rollout contract still requires explicit revision handoff and rollback
- release-gate posture remains present
- secrets posture remains clean
- workflow-level permissions remain `contents: read`

## Review Outcomes

### 1. `rollout_stage_controlled_patch_blocked`

Required when:

- the reviewed diff touches any job beyond `ecs-rollout-placeholder`
- workflow-level permissions are widened
- `public-verification-placeholder` changes
- live ECS behavior bypasses immutable image truth or rollback posture
- the Flask application contract is touched

### 2. `rollout_stage_controlled_patch_review_required`

Allowed when:

- the reviewed diff is narrow enough
- the patch remains second-job-only
- immutable image truth, rollback posture, and release-gate posture remain explicit
- operator review is still required before any patch mission

### 3. `rollout_stage_controlled_patch_ready_for_patch_mission`

Allowed when:

- the reviewed diff is limited to the rollout job hunk
- `push-image-placeholder` remains unchanged
- `public-verification-placeholder` remains unchanged and disabled
- workflow-level permissions remain unchanged
- all preserved posture evidence still holds
- the patch remains bounded by the reviewed rollout truth chain

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `rollout_stage_controlled_patch_ready_for_patch_mission`, the
following remain forbidden in this mission:

- modifying `push-image-placeholder`
- modifying `public-verification-placeholder`
- widening workflow-level permissions
- bypassing immutable image truth, rollback posture, or release-gate posture
- changing `app.py`
- introducing static AWS credentials

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/ecs-rollout-stage-controlled-patch-review.template.json`](./.github/ecs-rollout-stage-controlled-patch-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not a patch token.

## Source Boundary

Source may contain:

- reviewed patch scope
- preserved required lines
- blocked/review/ready outcomes
- explicit forbidden actions

Source must not contain:

- live AWS commands outside the reviewed second-job boundary
- credentials
- hidden enablement flags
- a patched workflow body in this mission

## Governance Rules

- the rollout-stage controlled patch review must remain downstream of the
  rollout-stage proposal
- the rollout-stage controlled patch review must remain narrower than actual job
  enablement
- `public-verification-placeholder` must stay blocked
- the Flask service contract must remain untouched

## Explicit Non-Goals

This review does not:

- patch the workflow
- enable any job
- create AWS trust
- create deployment automation
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CANDIDATE_REVIEW_V1.md)
- [`.github/ecs-rollout-stage-controlled-patch-review.template.json`](./.github/ecs-rollout-stage-controlled-patch-review.template.json)
- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_PATCH_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_PATCH_V1.md)
- [`.github/ecs-rollout-stage-patch.template.json`](./.github/ecs-rollout-stage-patch.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `First Bounded ECS Rollout Run v1`

That mission should execute only the already-reviewed second-job path while
preserving push-image behavior, public-verification disablement, immutable
image truth, rollback posture, and release-gate discipline.

## Warning

Do not treat this review as permission to patch the workflow freely.

It only defines the exact narrow review boundary a later rollout-stage patch
must obey.
