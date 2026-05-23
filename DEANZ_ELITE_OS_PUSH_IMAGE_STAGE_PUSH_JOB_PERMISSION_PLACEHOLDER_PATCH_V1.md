# Dean'z Elite OS Push Image Stage Push-Job Permission Placeholder Patch v1

## Purpose

This document records the first bounded permission-placeholder patch applied to
the `push-image-placeholder` job inside the `task-planner-foundation`
deployment workflow skeleton.

It exists to answer these questions after the permission-widening review:

- what exact first-job permission-placeholder hunk was changed?
- what critical lines remained preserved?
- what future job-local permission posture is now visible in source?
- why does the workflow still remain disabled and non-deploying?

This document does not:

- enable `push-image-placeholder`
- add a real job-local `permissions` block
- widen workflow-level permissions
- authenticate to AWS
- log in to ECR
- push an image
- change the Flask application contract

## Scope

This permission-placeholder patch applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_WIDENING_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_WIDENING_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the already-reviewed future permission hunk for the first
disabled job.

## Patch Objective

This patch exists to make the future first-job permission posture explicit
while preserving zero deploy power.

The applied patch must remain:

- `permission_placeholder_patch_applied`
- `permission_placeholder_patch_still_disabled`
- `permission_placeholder_patch_still_non_deploying`

## Applied Patch Footprint

The applied patch remains limited to the `push-image-placeholder` job.

The patch changed only:

- comments directly above `push-image-placeholder`
- one new placeholder step name inside that job
- placeholder `echo` lines describing the future permission shape

The patch did not change:

- workflow-level `permissions`
- job-level `permissions`
- `activation-gate-summary`
- `ecs-rollout-placeholder`
- `public-verification-placeholder`
- workflow trigger shape
- workflow service scope

## Preserved Required Lines

The patch preserved these critical workflow lines:

1. `push-image-placeholder`
2. `if: ${{ false }}`
3. `needs: activation-gate-summary`
4. workflow-level `permissions: contents: read`
5. manual-only `workflow_dispatch`

## Added Permission Placeholder Guidance

The patch adds only source-visible placeholder guidance for future missions:

- future job-local permission placement must remain on `push-image-placeholder` only
- future job-local permission shape must remain `contents: read` plus `id-token: write`
- future workflow-level permissions must remain `contents: read`
- future later-stage jobs must remain without permission changes
- no live permission change, auth action, login, push, or static credentials are allowed in this mission

These additions are visible reminders only.

They do not introduce live permission behavior.

## Prohibited Content That Remains Absent

The applied patch still does not contain:

- a job-level `permissions` block
- workflow-level permission widening
- `aws-actions/configure-aws-credentials`
- `aws ecr get-login-password`
- `docker login`
- `docker push`
- any AWS-mutating command
- any static AWS credentials

## Outcome

The result of this patch is intentionally narrow:

- the first job now records the future permission posture
- the job is still disabled
- workflow permissions remain unchanged
- later jobs are still disabled
- no deploy authority has been introduced

## Canonical Planning Artifact

The non-secret planning artifact for this patch is:

- [`.github/push-image-stage-push-job-permission-placeholder-patch.template.json`](./.github/push-image-stage-push-job-permission-placeholder-patch.template.json)

That file records the preserved lines, added permission-placeholder messages,
and still-forbidden actions for this first job hunk.

## Source Boundary

Source may contain:

- patched comments
- patched placeholder step name
- patched placeholder `echo` lines
- preserved-line summary

Source must not contain:

- live permission changes
- credentials
- auth/login/push commands
- workflow changes outside the first job hunk

## Governance Rules

- the permission-placeholder patch must remain downstream of the permission review
- the patched job must remain disabled
- workflow permissions must remain unchanged in this mission
- later jobs must remain unchanged
- application code must remain untouched

## Explicit Non-Goals

This patch does not:

- enable any job
- create AWS trust
- create deployment automation
- widen permissions in source
- authenticate to AWS
- log in to ECR
- push an image
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_WIDENING_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_WIDENING_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-push-job-permission-placeholder-patch.template.json`](./.github/push-image-stage-push-job-permission-placeholder-patch.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_INVOCATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_INVOCATION_REVIEW_V1.md)
- [`.github/push-image-stage-oidc-auth-action-invocation-review.template.json`](./.github/push-image-stage-oidc-auth-action-invocation-review.template.json)

## Recommended Next Mission

The next bounded step after this patch should be:

- `Push Image Stage OIDC Auth Action Invocation Review v1`

That mission should remain review-only and define the exact future auth-action
invocation posture after permissions, auth, login, and push placeholders are all
visible in source.

## Warning

Do not treat this patch as permission to widen workflow behavior.

It only records the future job-local permission posture in the first disabled
job while preserving the non-deploying foundation posture.
