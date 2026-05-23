# Dean'z Elite OS Push Image Stage ECR Login Shape Review v1

## Purpose

This document defines the first bounded ECR-login shape review for the
`push-image-placeholder` job inside the `task-planner-foundation` deployment
workflow skeleton.

It exists to answer these questions before any registry-login command is ever
introduced:

- where may a future ECR login step appear?
- what auth dependency must already be present before it is reviewable?
- what exact login posture is acceptable for the first job?
- what must still remain absent even after the login shape is reviewed?

This document does not:

- add an ECR login step to the workflow
- authenticate to AWS
- push an image
- create AWS trust
- change the Flask application contract

## Scope

This ECR-login shape review applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact future ECR-login posture for the first disabled job.

## Login Shape Review Objective

This review exists to decide whether the future ECR login step remains:

- `ecr_login_shape_blocked`
- `ecr_login_shape_review_required`
- `ecr_login_shape_ready_for_placeholder_login_patch`

This is still not a workflow patch action.

## Future ECR Login Placement

The only future login step in scope is a single job-local registry-login step
inside `push-image-placeholder`.

It may appear only:

- inside `push-image-placeholder`
- after a future job-local OIDC auth step
- before any future image-push step

It must not appear in:

- `activation-gate-summary`
- `ecs-rollout-placeholder`
- `public-verification-placeholder`
- any other workflow file

## Future Login Shape

The future login posture must remain explicit and narrow.

The reviewed shape may reference only:

- an ECR registry URI derived from the approved parameter boundary
- a region value from a non-secret parameter source
- the standard `aws ecr get-login-password` to `docker login --password-stdin` pattern

The reviewed shape must not include:

- inline passwords
- inline secret values
- registry wildcards with no explicit account/region posture
- push commands bundled into the same reviewed step

## Required Upstream Evidence

Immediately before any future login-placeholder patch is allowed to start,
these must still be true:

- `app.py` has no diff
- `push-image-placeholder` remains disabled
- the OIDC auth-placeholder patch remains intact
- GitHub OIDC trust posture still matches this repo and `main`
- immutable image tag posture remains `sha-<git-sha>`
- ECR promotion contract still requires immutable rollout identity
- later jobs remain unchanged and disabled
- secrets posture remains clean

## Login Shape Constraints

Even if the login shape becomes review-ready, the following must remain absent:

- live OIDC auth action usage
- image-push commands
- ECS rollout commands
- public verification commands
- static AWS credentials
- changes to later-stage jobs

The login shape review must stop before any state-changing or registry-mutating
behavior enters source.

## Review Outcomes

### 1. `ecr_login_shape_blocked`

Required when:

- login placement is outside `push-image-placeholder`
- auth dependency posture is missing or widened
- static credentials are proposed
- login shape is bundled with image-push behavior
- later jobs are touched

### 2. `ecr_login_shape_review_required`

Allowed when:

- the future login shape is narrow enough
- the job remains disabled
- the future login posture is still review-only
- operator review is still required before any login-placeholder patch

### 3. `ecr_login_shape_ready_for_placeholder_login_patch`

Allowed when:

- the future login step is confined to `push-image-placeholder`
- OIDC auth dependency remains explicit
- login posture remains registry-login only
- all upstream evidence still holds

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `ecr_login_shape_ready_for_placeholder_login_patch`, the following
remain forbidden in this mission:

- enabling `push-image-placeholder`
- adding a live login step
- adding image push behavior
- adding ECS rollout behavior
- modifying later-stage jobs
- introducing static AWS credentials

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/push-image-stage-ecr-login-shape-review.template.json`](./.github/push-image-stage-ecr-login-shape-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not a registry token.

## Source Boundary

Source may contain:

- reviewed future login-step placement
- reviewed login command shape
- reviewed upstream evidence
- blocked/review/ready outcomes

Source must not contain:

- live login commands
- credentials
- image-push commands
- a widened workflow outside the first job

## Governance Rules

- ECR-login shape review must remain downstream of the OIDC auth-placeholder patch
- ECR-login shape review must remain downstream of the rollout contract
- ECR-login shape review must remain narrower than an actual login-placeholder patch
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

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/push-image-stage-ecr-login-shape-review.template.json`](./.github/push-image-stage-ecr-login-shape-review.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_INVOCATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_INVOCATION_REVIEW_V1.md)
- [`.github/push-image-stage-ecr-login-command-invocation-review.template.json`](./.github/push-image-stage-ecr-login-command-invocation-review.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `Push Image Stage ECR Login Command Invocation Review v1`

That mission should remain review-only and define the exact future registry-login
command invocation posture before any placeholder-login patch is introduced.

## Warning

Do not treat this review as permission to add live ECR login.

It only defines the exact future registry-login posture a later
placeholder-login patch must obey.
