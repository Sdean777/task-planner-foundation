# Dean'z Elite OS Push Image Stage OIDC Auth Action Invocation Review v1

## Purpose

This document defines the first bounded OIDC auth-action invocation review for
the `push-image-placeholder` job inside the `task-planner-foundation`
deployment workflow skeleton.

It exists to answer these questions before any auth action reference is ever
introduced:

- where may a future auth action invocation appear?
- what exact action and version posture is acceptable for the first job?
- which inputs may be referenced explicitly?
- what must still remain absent even after the invocation shape is reviewed?

This document does not:

- add an auth action to the workflow
- change workflow or job permissions
- enable `push-image-placeholder`
- authenticate to AWS
- log in to ECR
- push an image
- change the Flask application contract

## Scope

This auth-action review applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact future auth-action invocation posture for the first
disabled job.

## Invocation Review Objective

This review exists to decide whether the future auth action remains:

- `auth_action_invocation_blocked`
- `auth_action_invocation_review_required`
- `auth_action_invocation_ready_for_placeholder_patch`

This is still not a workflow patch action.

## Future Auth Action Placement

The only future auth action in scope is a single job-local action step inside
`push-image-placeholder`.

It may appear only:

- inside `push-image-placeholder`
- after a future job-local `permissions` block is reviewed
- before any future ECR login or image-push step

It must not appear in:

- `activation-gate-summary`
- `ecs-rollout-placeholder`
- `public-verification-placeholder`
- any other workflow file

## Future Auth Action Shape

The future auth action posture must remain explicit and narrow.

The reviewed invocation may reference only:

- `aws-actions/configure-aws-credentials@v4`
- `role-to-assume`
- `aws-region`
- `role-session-name`

The reviewed invocation must not reference:

- `aws-access-key-id`
- `aws-secret-access-key`
- session tags or extra role-chaining features beyond first-job scope
- alternate auth actions with broader or unclear posture
- inline credentials or hidden secret shortcuts

## Required Upstream Evidence

Immediately before any future auth-action-placeholder patch is allowed to
start, these must still be true:

- `app.py` has no diff
- `push-image-placeholder` remains disabled
- the permission-placeholder patch remains intact
- the GitHub OIDC auth-placeholder patch remains intact
- GitHub OIDC trust posture still matches this repo and `main`
- workflow-level permissions remain `contents: read`
- later jobs remain unchanged and disabled
- secrets posture remains clean

## Invocation Constraints

Even if the invocation shape becomes review-ready, the following must remain
absent:

- live auth action invocation in workflow source
- live ECR login commands
- live image-push commands
- workflow-level permission changes
- later-stage job modifications
- static AWS credentials

The invocation review must stop before any action reference enters source.

## Review Outcomes

### 1. `auth_action_invocation_blocked`

Required when:

- invocation placement is outside `push-image-placeholder`
- action shape widens beyond the reviewed invocation
- static credentials are proposed
- auth invocation is bundled with login or push behavior
- later jobs are touched

### 2. `auth_action_invocation_review_required`

Allowed when:

- the future invocation shape is narrow enough
- the job remains disabled
- the future invocation posture is still review-only
- operator review is still required before any auth-action-placeholder patch

### 3. `auth_action_invocation_ready_for_placeholder_patch`

Allowed when:

- the future auth action is confined to `push-image-placeholder`
- invocation shape remains `aws-actions/configure-aws-credentials@v4`
- reviewed inputs remain explicit and bounded
- all upstream evidence still holds

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `auth_action_invocation_ready_for_placeholder_patch`, the following
remain forbidden in this mission:

- enabling `push-image-placeholder`
- adding a live auth action
- adding ECR login behavior
- adding image-push behavior
- modifying later-stage jobs
- introducing static AWS credentials

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/push-image-stage-oidc-auth-action-invocation-review.template.json`](./.github/push-image-stage-oidc-auth-action-invocation-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not an auth token.

## Source Boundary

Source may contain:

- reviewed future action placement
- reviewed action/version choice
- reviewed explicit inputs
- blocked/review/ready outcomes

Source must not contain:

- live action invocation
- credentials
- login/push commands
- a widened workflow outside the first job

## Governance Rules

- auth-action invocation review must remain downstream of the permission-placeholder patch
- auth-action invocation review must remain downstream of the OIDC trust contract
- auth-action invocation review must remain narrower than an actual auth-action-placeholder patch
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

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-oidc-auth-action-invocation-review.template.json`](./.github/push-image-stage-oidc-auth-action-invocation-review.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-oidc-auth-action-placeholder-patch.template.json`](./.github/push-image-stage-oidc-auth-action-placeholder-patch.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `Push Image Stage OIDC Auth Action Placeholder Patch v1`

That mission should remain disabled and non-deploying while recording the
future auth-action invocation posture directly in the first job without adding
live authentication behavior.

## Warning

Do not treat this review as permission to invoke live auth actions.

It only defines the exact future auth-action posture a later placeholder patch
must obey.
