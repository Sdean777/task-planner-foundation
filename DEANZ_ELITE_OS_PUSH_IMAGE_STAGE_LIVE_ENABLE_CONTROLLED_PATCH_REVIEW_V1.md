# Dean'z Elite OS Push Image Stage Live-Enable Controlled Patch Review v1

## Purpose

This document defines the refreshed bounded controlled-patch review for the
`push-image-placeholder` job inside the `task-planner-foundation` deployment
workflow skeleton.

It exists to answer these questions before any future live-enable patch is
considered:

- what exact workflow hunk is reviewable for a future live-enable attempt?
- what lines must remain unchanged inside that hunk?
- what evidence must still be rechecked immediately before any future patch?
- how does the reviewed patch remain first-job-only and bounded by trust,
  rollback, release-gate, and immutable-tag posture?

This document does not:

- patch the workflow
- enable `push-image-placeholder`
- add AWS authentication
- log in to ECR
- push an image to ECR
- change the Flask application contract

## Scope

This controlled-patch review applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact first-job live-enable patch-review boundary.

## Controlled Patch Review Objective

This review exists to decide whether the refreshed first workflow patch
remains:

- `live_enable_controlled_patch_blocked`
- `live_enable_controlled_patch_review_required`
- `live_enable_controlled_patch_ready_for_patch_mission`

This is still not a workflow patch action.

## Reviewed Patch Target

The only workflow hunk in scope is the `push-image-placeholder` job.

The reviewed patch may touch only:

- the `if: ${{ false }}` gate for that job
- a job-local `permissions` block for that job only
- comments directly above that job
- job-local step ordering inside that job
- job-local lines required to preserve later-job disablement and immutable
  image identity

The reviewed patch must not touch:

- `activation-gate-summary`
- `ecs-rollout-placeholder`
- `public-verification-placeholder`
- workflow trigger shape
- workflow service scope
- workflow-level permissions

## Exact Patch Boundaries

The refreshed reviewed patch must remain narrow enough that trust and rollout
discipline stay visible and auditable.

Allowed reviewed patch shape:

1. change only the `push-image-placeholder` job
2. preserve `needs: activation-gate-summary`
3. preserve the job name `push-image-placeholder`
4. preserve `workflow_dispatch` as the only trigger
5. preserve workflow-level `permissions: contents: read`
6. preserve later jobs as disabled and unchanged
7. keep rollout identity subordinate to immutable `sha-<git-sha>` truth

The reviewed patch may describe or position future first-job behavior, but it
must not widen beyond the first job.

## Allowed Reviewed Patch Content

The refreshed reviewed patch may contain only:

- a re-evaluated first-job `if:` gate for `push-image-placeholder`
- a job-local `permissions` block no wider than `contents: read` plus
  `id-token: write`
- a single job-local auth-action step shape already defined by the existing
  placeholder chain
- a single job-local ECR-login command shape already defined by the existing
  placeholder chain
- a single job-local image-push shape subordinate to immutable
  `sha-<git-sha>` rollout identity
- clarifying comments or ordering that preserve later-job disablement and
  release-gate posture

The refreshed reviewed patch must not contain:

- any change to workflow-level permissions
- any ECS rollout command
- any public verification command
- any application-code change
- any static AWS credential
- any hidden enablement flag outside `push-image-placeholder`

## Required Preserved Posture

Immediately before a later live-enable patch mission is allowed to start,
these must still be true:

- `app.py` has no diff
- `push-image-placeholder` remains the only in-scope job
- later jobs remain disabled and unchanged
- container-build verification remains present
- GitHub OIDC trust posture remains bounded to repo, branch, audience, and
  environment
- immutable tag posture remains `sha-<git-sha>`
- protected environment posture remains `production` on `main`
- release-gate posture remains present
- secrets posture remains clean
- workflow-level permissions remain `contents: read`

## Review Outcomes

### 1. `live_enable_controlled_patch_blocked`

Required when:

- the reviewed diff touches any job beyond `push-image-placeholder`
- workflow-level permissions are widened
- later jobs are changed
- live AWS behavior bypasses preserved trust or rollback posture
- the Flask application contract is touched

### 2. `live_enable_controlled_patch_review_required`

Allowed when:

- the reviewed diff is narrow enough
- the patch remains first-job-only
- trust, rollback, release-gate, and immutable-tag posture remain explicit
- operator review is still required before any patch mission

### 3. `live_enable_controlled_patch_ready_for_patch_mission`

Allowed when:

- the reviewed diff is limited to the first job hunk
- later jobs remain unchanged and disabled
- workflow-level permissions remain unchanged
- all preserved posture evidence still holds
- the patch remains bounded by the reviewed first-job trust chain

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `live_enable_controlled_patch_ready_for_patch_mission`, the
following remain forbidden in this mission:

- modifying `ecs-rollout-placeholder`
- modifying `public-verification-placeholder`
- widening workflow-level permissions
- bypassing immutable tag, rollback, or release-gate posture
- changing `app.py`
- introducing static AWS credentials

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/push-image-stage-live-enable-controlled-patch-review.template.json`](./.github/push-image-stage-live-enable-controlled-patch-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not a patch token.

## Source Boundary

Source may contain:

- reviewed patch scope
- preserved required lines
- blocked/review/ready outcomes
- explicit forbidden actions

Source must not contain:

- live AWS commands outside the reviewed first-job boundary
- credentials
- hidden enablement flags
- a patched workflow body in this mission

## Governance Rules

- the live-enable controlled patch review must remain downstream of the
  live-enable proposal
- the live-enable controlled patch review must remain narrower than actual job
  enablement
- later jobs must stay blocked
- the Flask service contract must remain untouched

## Explicit Non-Goals

This contract does not:

- patch the workflow
- enable any job
- create AWS trust
- create deployment automation
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md)
- [`.github/push-image-stage-live-enable-controlled-patch-review.template.json`](./.github/push-image-stage-live-enable-controlled-patch-review.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PATCH_V1.md)
- [`.github/push-image-stage-live-enable-patch.template.json`](./.github/push-image-stage-live-enable-patch.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `Push Image Stage Live-Enable Patch v1`

That mission should apply only the already-reviewed first-job diff while
preserving later-job disablement, immutable rollout identity, and release-gate
discipline.

## Warning

Do not treat this review as permission to patch the workflow freely.

It only defines the exact narrow review boundary a later first-job live-enable
patch must obey.
