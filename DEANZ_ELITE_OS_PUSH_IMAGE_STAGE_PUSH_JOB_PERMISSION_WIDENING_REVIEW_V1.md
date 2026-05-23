# Dean'z Elite OS Push Image Stage Push-Job Permission Widening Review v1

## Purpose

This document defines the first bounded permission-widening review for the
`push-image-placeholder` job inside the `task-planner-foundation` deployment
workflow skeleton.

It exists to answer these questions before any workflow-level or job-level
permission change is ever introduced:

- where may future permission widening appear?
- what exact permission shape is acceptable for the first job?
- which permissions must remain absent?
- what upstream evidence must still hold before a permission patch is even reviewable?

This document does not:

- change workflow permissions
- change job-level permissions
- enable `push-image-placeholder`
- add AWS authentication
- log in to ECR
- push an image
- change the Flask application contract

## Scope

This permission-widening review applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact future permission posture for the first disabled job.

## Permission Review Objective

This review exists to decide whether the future permission change remains:

- `permission_widening_blocked`
- `permission_widening_review_required`
- `permission_widening_ready_for_placeholder_patch`

This is still not a workflow patch action.

## Future Permission Placement

The only future permission widening in scope is a single job-local `permissions`
block on `push-image-placeholder`.

It may appear only:

- on `push-image-placeholder`
- without changing the workflow-level `permissions` block
- without touching any later-stage job

It must not appear in:

- `activation-gate-summary`
- `ecs-rollout-placeholder`
- `public-verification-placeholder`
- workflow-level `permissions`
- any other workflow file

## Future Permission Shape

The future job-local permission posture must remain explicit and minimal.

The reviewed shape may contain only:

- `contents: read`
- `id-token: write`

The reviewed shape must not contain:

- `contents: write`
- `packages: write`
- `actions: write`
- `deployments: write`
- `issues: write`
- `pull-requests: write`
- wildcard or blanket permission grants

The current workflow-level `permissions: contents: read` must remain unchanged
in this review posture.

## Required Upstream Evidence

Immediately before any future permission-placeholder patch is allowed to
start, these must still be true:

- `app.py` has no diff
- `push-image-placeholder` remains disabled
- the GitHub OIDC auth-placeholder patch remains intact
- the ECR-login placeholder patch remains intact
- the image-push placeholder patch remains intact
- GitHub OIDC trust posture still matches this repo and `main`
- later jobs remain unchanged and disabled
- secrets posture remains clean

## Permission Constraints

Even if the permission shape becomes review-ready, the following must remain
absent:

- live `aws-actions/configure-aws-credentials`
- live ECR login commands
- live image-push commands
- workflow-level permission widening
- later-stage job modifications
- static AWS credentials

The permission review must stop before any permission change enters source.

## Review Outcomes

### 1. `permission_widening_blocked`

Required when:

- permissions are widened beyond `contents: read` and `id-token: write`
- workflow-level permissions are touched
- later jobs are touched
- permission widening is bundled with auth, login, or push commands
- static credentials are proposed

### 2. `permission_widening_review_required`

Allowed when:

- the future permission shape is narrow enough
- the job remains disabled
- the future permission posture is still review-only
- operator review is still required before any permission-placeholder patch

### 3. `permission_widening_ready_for_placeholder_patch`

Allowed when:

- the future permission block is confined to `push-image-placeholder`
- the shape remains `contents: read` plus `id-token: write`
- workflow-level permissions remain unchanged
- all upstream evidence still holds

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `permission_widening_ready_for_placeholder_patch`, the following
remain forbidden in this mission:

- enabling `push-image-placeholder`
- changing workflow-level permissions
- widening permissions beyond the reviewed shape
- adding auth, login, or push commands
- modifying later-stage jobs
- introducing static AWS credentials

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/push-image-stage-push-job-permission-widening-review.template.json`](./.github/push-image-stage-push-job-permission-widening-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not a permission token.

## Source Boundary

Source may contain:

- reviewed future permission placement
- reviewed minimal permission shape
- reviewed upstream evidence
- blocked/review/ready outcomes

Source must not contain:

- live permission changes
- credentials
- auth/login/push commands
- a widened workflow outside the first job

## Governance Rules

- permission-widening review must remain downstream of the image-push placeholder patch
- permission-widening review must remain downstream of the auth-shape doctrine
- permission-widening review must remain narrower than an actual permission-placeholder patch
- later jobs must stay blocked
- application code must remain untouched

## Explicit Non-Goals

This contract does not:

- patch the workflow
- enable any job
- widen permissions in source
- authenticate to AWS
- log in to ECR
- push an image
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-push-job-permission-widening-review.template.json`](./.github/push-image-stage-push-job-permission-widening-review.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-push-job-permission-placeholder-patch.template.json`](./.github/push-image-stage-push-job-permission-placeholder-patch.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `Push Image Stage Push-Job Permission Placeholder Patch v1`

That mission should remain disabled and non-deploying while recording the
future job-local permission block directly in the first job without changing
workflow-level permissions.

## Warning

Do not treat this review as permission to widen workflow behavior.

It only defines the exact future job-local permission posture a later
placeholder-permission patch must obey.
