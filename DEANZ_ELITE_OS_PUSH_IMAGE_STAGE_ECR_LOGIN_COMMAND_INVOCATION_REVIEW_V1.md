# Dean'z Elite OS Push Image Stage ECR Login Command Invocation Review v1

## Purpose

This document defines the first bounded ECR-login command invocation review for
the `push-image-placeholder` job inside the `task-planner-foundation`
deployment workflow skeleton.

It exists to answer these questions before any registry-login command
reference is ever introduced:

- where may a future ECR-login command invocation appear?
- what exact command posture is acceptable for the first job?
- which command inputs may be referenced explicitly?
- what must still remain absent even after the invocation shape is reviewed?

This document does not:

- add an ECR-login command to the workflow
- authenticate to AWS
- enable `push-image-placeholder`
- push an image
- create AWS trust
- change the Flask application contract

## Scope

This command-invocation review applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact future login-command invocation posture for the first
disabled job.

## Invocation Review Objective

This review exists to decide whether the future login command remains:

- `login_command_invocation_blocked`
- `login_command_invocation_review_required`
- `login_command_invocation_ready_for_placeholder_patch`

This is still not a workflow patch action.

## Future Command Placement

The only future registry-login command in scope is a single job-local command
step inside `push-image-placeholder`.

It may appear only:

- inside `push-image-placeholder`
- after a future auth-action step
- before any future image-push step

It must not appear in:

- `activation-gate-summary`
- `ecs-rollout-placeholder`
- `public-verification-placeholder`
- any other workflow file

## Future Command Shape

The future login-command posture must remain explicit and narrow.

The reviewed command shape may reference only:

- `aws ecr get-login-password`
- `docker login --username AWS --password-stdin`
- an explicit AWS region input
- an explicit ECR registry URI from approved non-secret boundaries

The reviewed command shape must not reference:

- inline passwords
- inline secret values
- wildcard or implicit registry targets
- chained image-push behavior in the same step
- alternate login flows with broader or less explicit posture

## Required Upstream Evidence

Immediately before any future login-command-placeholder patch is allowed to
start, these must still be true:

- `app.py` has no diff
- `push-image-placeholder` remains disabled
- the OIDC auth-action placeholder patch remains intact
- the push-job permission placeholder patch remains intact
- GitHub OIDC trust posture still matches this repo and `main`
- workflow-level permissions remain `contents: read`
- later jobs remain unchanged and disabled
- secrets posture remains clean

## Invocation Constraints

Even if the login-command shape becomes review-ready, the following must remain
absent:

- live auth action invocation in workflow source
- live login command invocation in workflow source
- live image-push commands
- workflow-level permission changes
- later-stage job modifications
- static AWS credentials

The invocation review must stop before any command reference enters source.

## Review Outcomes

### 1. `login_command_invocation_blocked`

Required when:

- invocation placement is outside `push-image-placeholder`
- command shape widens beyond the reviewed invocation
- static credentials are proposed
- login invocation is bundled with image-push behavior
- later jobs are touched

### 2. `login_command_invocation_review_required`

Allowed when:

- the future invocation shape is narrow enough
- the job remains disabled
- the future invocation posture is still review-only
- operator review is still required before any login-command-placeholder patch

### 3. `login_command_invocation_ready_for_placeholder_patch`

Allowed when:

- the future login command is confined to `push-image-placeholder`
- reviewed command shape remains explicit and bounded
- reviewed inputs remain explicit and non-secret
- all upstream evidence still holds

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `login_command_invocation_ready_for_placeholder_patch`, the
following remain forbidden in this mission:

- enabling `push-image-placeholder`
- adding a live login command
- adding image-push behavior
- modifying later-stage jobs
- introducing static AWS credentials

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/push-image-stage-ecr-login-command-invocation-review.template.json`](./.github/push-image-stage-ecr-login-command-invocation-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not a registry token.

## Source Boundary

Source may contain:

- reviewed future command placement
- reviewed explicit command posture
- reviewed explicit inputs
- blocked/review/ready outcomes

Source must not contain:

- live command invocation
- credentials
- push commands
- a widened workflow outside the first job

## Governance Rules

- login-command invocation review must remain downstream of the auth-action placeholder patch
- login-command invocation review must remain downstream of the ECR-login doctrine
- login-command invocation review must remain narrower than an actual login-command-placeholder patch
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

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-ecr-login-command-invocation-review.template.json`](./.github/push-image-stage-ecr-login-command-invocation-review.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-ecr-login-command-placeholder-patch.template.json`](./.github/push-image-stage-ecr-login-command-placeholder-patch.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `Push Image Stage ECR Login Command Placeholder Patch v1`

That mission should remain disabled and non-deploying while recording the
future registry-login command posture directly in the first job without adding
live login behavior.

## Warning

Do not treat this review as permission to invoke live login commands.

It only defines the exact future registry-login command posture a later
placeholder patch must obey.
