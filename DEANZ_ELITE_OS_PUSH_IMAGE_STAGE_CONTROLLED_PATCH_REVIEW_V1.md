# Dean'z Elite OS Push Image Stage Controlled Patch Review v1

## Purpose

This document defines the first bounded controlled-patch review for the
`push-image-placeholder` job inside the `task-planner-foundation` deployment
workflow skeleton.

It exists to answer these questions before any workflow patch is applied:

- what exact workflow hunk is reviewable?
- what lines must remain unchanged inside that hunk?
- what evidence must still be rechecked immediately before a patch?
- how does the patch remain placeholder-bound and non-deploying?

This document does not:

- patch the workflow
- enable `push-image-placeholder`
- add AWS authentication
- push an image to ECR
- change the Flask application contract

## Scope

This controlled-patch review applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact first-job patch review boundary.

## Controlled Patch Review Objective

This review exists to decide whether the first workflow patch remains:

- `controlled_patch_blocked`
- `controlled_patch_review_required`
- `controlled_patch_ready_for_placeholder_patch`

This is still not a workflow patch action.

## Reviewed Patch Target

The only workflow hunk in scope is the `push-image-placeholder` job.

The reviewed patch may touch only:

- comments directly above that job
- job-local explanatory lines inside that job
- placeholder `echo` lines inside that job

The reviewed patch must not touch:

- `activation-gate-summary`
- `ecs-rollout-placeholder`
- `public-verification-placeholder`
- workflow trigger shape
- workflow service scope

## Exact Patch Boundaries

The first reviewed patch must remain narrow enough that the workflow still has
no deploy power.

Allowed patch shape:

1. preserve `if: ${{ false }}`
2. preserve `needs: activation-gate-summary`
3. preserve the job name `push-image-placeholder`
4. add only comment or `echo`-based placeholder clarification
5. preserve the manual-only `workflow_dispatch` trigger

The reviewed patch may describe future behavior, but it must not introduce live
behavior.

## Allowed Patch Content

The first reviewed patch may contain only:

- clarifying comments about future AWS auth or ECR push posture
- additional `echo` lines referencing future immutable tag use
- additional `echo` lines referencing future protected-environment posture
- narrow read-only metadata such as step names or comments

The first reviewed patch must not contain:

- `aws-actions/configure-aws-credentials`
- `aws ecr` commands
- `docker login`
- `docker push`
- any command that mutates AWS state
- any command that requires a secret

## Required Preserved Posture

Immediately before a later patch mission is allowed to start, these must still
be true:

- `app.py` has no diff
- `push-image-placeholder` remains disabled with `if: ${{ false }}`
- later jobs remain disabled and unchanged
- container-build verification remains present
- GitHub OIDC trust posture remains planning-only
- immutable tag posture remains `sha-<git-sha>`
- protected environment posture remains `production` on `main`
- secrets posture remains clean

## Review Outcomes

### 1. `controlled_patch_blocked`

Required when:

- the reviewed diff touches any job beyond `push-image-placeholder`
- `if: ${{ false }}` is removed or weakened
- live AWS or ECR commands are introduced
- the workflow trigger shape changes
- the Flask application contract is touched

### 2. `controlled_patch_review_required`

Allowed when:

- the reviewed diff is narrow enough
- the job stays disabled
- the patch remains placeholder-bound
- operator review is still required before any patch mission

### 3. `controlled_patch_ready_for_placeholder_patch`

Allowed when:

- the reviewed diff is limited to the first job hunk
- later jobs remain unchanged and disabled
- the patch contains only comment or `echo`-based placeholders
- all preserved posture evidence still holds

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `controlled_patch_ready_for_placeholder_patch`, the following remain
forbidden in this mission:

- enabling `push-image-placeholder`
- modifying `ecs-rollout-placeholder`
- modifying `public-verification-placeholder`
- adding AWS credentials or OIDC auth steps
- adding ECR login or image-push commands
- adding ECS rollout or public verification behavior

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/push-image-stage-controlled-patch-review.template.json`](./.github/push-image-stage-controlled-patch-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not a patch token.

## Source Boundary

Source may contain:

- reviewed patch scope
- preserved required lines
- blocked/review/ready outcomes
- explicit forbidden actions

Source must not contain:

- live AWS commands
- credentials
- hidden enablement flags
- a patched workflow body

## Governance Rules

- the controlled patch review must remain narrower than the enablement proposal
- the controlled patch review must remain narrower than actual workflow mutation
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

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md)
- [`.github/push-image-stage-controlled-patch-review.template.json`](./.github/push-image-stage-controlled-patch-review.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md)
- [`.github/push-image-stage-placeholder-bound-patch.template.json`](./.github/push-image-stage-placeholder-bound-patch.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `Push Image Stage Placeholder-Bound Patch v1`

That mission should apply only the already-reviewed first-job placeholder hunk
while keeping the workflow disabled and non-deploying.

## Warning

Do not treat this review as permission to patch the workflow freely.

It only defines the exact narrow review boundary a later first-job patch must
obey.
