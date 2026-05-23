# Dean'z Elite OS Push Image Stage Image Push Shape Review v1

## Purpose

This document defines the first bounded image-push shape review for the
`push-image-placeholder` job inside the `task-planner-foundation` deployment
workflow skeleton.

It exists to answer these questions before any image-push command is ever
introduced:

- where may a future image-push step appear?
- what auth and login dependencies must already be present before it is reviewable?
- what exact push posture is acceptable for the first job?
- what must still remain absent even after the push shape is reviewed?

This document does not:

- add an image-push step to the workflow
- authenticate to AWS
- log in to ECR
- push an image
- create AWS trust
- change the Flask application contract

## Scope

This image-push shape review applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact future image-push posture for the first disabled job.

## Push Shape Review Objective

This review exists to decide whether the future image-push step remains:

- `image_push_shape_blocked`
- `image_push_shape_review_required`
- `image_push_shape_ready_for_placeholder_push_patch`

This is still not a workflow patch action.

## Future Image Push Placement

The only future image-push step in scope is a single job-local push step inside
`push-image-placeholder`.

It may appear only:

- inside `push-image-placeholder`
- after a future OIDC auth step
- after a future ECR login step
- before any future ECS rollout step

It must not appear in:

- `activation-gate-summary`
- `ecs-rollout-placeholder`
- `public-verification-placeholder`
- any other workflow file

## Future Image Push Shape

The future push posture must remain explicit and narrow.

The reviewed shape may reference only:

- an immutable `sha-<git-sha>` image tag as rollout truth
- an optional `main` convenience tag only if it does not replace the SHA tag
- an explicit ECR registry/repository target from approved non-secret boundaries
- clearly ordered push behavior that publishes the immutable tag first

The reviewed shape must not include:

- `latest`
- ad hoc manual tags with no SHA linkage
- hidden retagging as rollout truth
- ECS rollout commands bundled into the same reviewed step

## Required Upstream Evidence

Immediately before any future push-placeholder patch is allowed to start,
these must still be true:

- `app.py` has no diff
- `push-image-placeholder` remains disabled
- the OIDC auth-placeholder patch remains intact
- the ECR-login placeholder patch remains intact
- GitHub OIDC trust posture still matches this repo and `main`
- immutable image tag posture remains `sha-<git-sha>`
- rollout contract still requires explicit revision-based rollout identity
- later jobs remain unchanged and disabled
- secrets posture remains clean

## Push Shape Constraints

Even if the push shape becomes review-ready, the following must remain absent:

- live OIDC auth action usage
- live ECR login commands
- ECS rollout commands
- public verification commands
- static AWS credentials
- changes to later-stage jobs

The push shape review must stop before any registry-mutating or rollout-bearing
behavior enters source.

## Review Outcomes

### 1. `image_push_shape_blocked`

Required when:

- push placement is outside `push-image-placeholder`
- auth or login dependency posture is missing or widened
- `latest` or non-traceable tags are proposed as rollout truth
- push shape is bundled with ECS rollout behavior
- later jobs are touched

### 2. `image_push_shape_review_required`

Allowed when:

- the future push shape is narrow enough
- the job remains disabled
- the future push posture is still review-only
- operator review is still required before any push-placeholder patch

### 3. `image_push_shape_ready_for_placeholder_push_patch`

Allowed when:

- the future push step is confined to `push-image-placeholder`
- auth and login dependency posture remains explicit
- push posture remains image-publication only
- all upstream evidence still holds

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `image_push_shape_ready_for_placeholder_push_patch`, the following
remain forbidden in this mission:

- enabling `push-image-placeholder`
- adding a live push step
- adding ECS rollout behavior
- adding public verification behavior
- modifying later-stage jobs
- introducing static AWS credentials

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/push-image-stage-image-push-shape-review.template.json`](./.github/push-image-stage-image-push-shape-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not a registry mutation token.

## Source Boundary

Source may contain:

- reviewed future push-step placement
- reviewed image-tag rules
- reviewed upstream evidence
- blocked/review/ready outcomes

Source must not contain:

- live push commands
- credentials
- rollout commands
- a widened workflow outside the first job

## Governance Rules

- image-push shape review must remain downstream of the ECR-login placeholder patch
- image-push shape review must remain downstream of the rollout contract
- image-push shape review must remain narrower than an actual push-placeholder patch
- later jobs must stay blocked
- application code must remain untouched

## Explicit Non-Goals

This contract does not:

- patch the workflow
- enable any job
- authenticate to AWS
- log in to ECR
- push an image
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/push-image-stage-image-push-shape-review.template.json`](./.github/push-image-stage-image-push-shape-review.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-image-push-placeholder-patch.template.json`](./.github/push-image-stage-image-push-placeholder-patch.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `Push Image Stage Image Push Placeholder Patch v1`

That mission should remain disabled and non-deploying while recording the
future image-push posture directly in the first job without introducing live
registry or deploy behavior.

## Warning

Do not treat this review as permission to add live image push.

It only defines the exact future image-push posture a later placeholder-push
patch must obey.
