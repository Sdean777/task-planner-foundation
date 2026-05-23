# Dean'z Elite OS Push Image Stage OIDC Auth Action Placeholder Patch v1

## Purpose

This document records the first bounded auth-action placeholder patch applied to
the `push-image-placeholder` job inside the `task-planner-foundation`
deployment workflow skeleton.

It exists to answer these questions after the auth-action invocation review:

- what exact first-job auth-action placeholder hunk was changed?
- what critical lines remained preserved?
- what future auth-action invocation posture is now visible in source?
- why does the workflow still remain disabled and non-deploying?

This document does not:

- enable `push-image-placeholder`
- add a live `uses:` auth action step
- widen workflow or job permissions
- authenticate to AWS
- log in to ECR
- push an image
- change the Flask application contract

## Scope

This auth-action placeholder patch applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_INVOCATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_INVOCATION_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the already-reviewed future auth-action hunk for the first
disabled job.

## Patch Objective

This patch exists to make the future first-job auth-action invocation posture
explicit while preserving zero deploy power.

The applied patch must remain:

- `auth_action_placeholder_patch_applied`
- `auth_action_placeholder_patch_still_disabled`
- `auth_action_placeholder_patch_still_non_deploying`

## Applied Patch Footprint

The applied patch remains limited to the `push-image-placeholder` job.

The patch changed only:

- comments directly above `push-image-placeholder`
- one new placeholder step name inside that job
- placeholder `echo` lines describing the future auth-action invocation shape

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

## Added Auth-Action Placeholder Guidance

The patch adds only source-visible placeholder guidance for future missions:

- future auth-action placement must remain inside `push-image-placeholder`
- future auth-action invocation must remain `aws-actions/configure-aws-credentials@v4`
- future explicit inputs must remain `role-to-assume`, `aws-region`, and `role-session-name`
- future auth-action placement must precede any ECR login or image-push behavior
- no live auth action, permission change, login, push, or static credentials are allowed in this mission

These additions are visible reminders only.

They do not introduce live auth-action behavior.

## Prohibited Content That Remains Absent

The applied patch still does not contain:

- a `uses: aws-actions/configure-aws-credentials@v4` step
- a job-level `permissions` block
- workflow-level permission widening
- `aws ecr get-login-password`
- `docker login`
- `docker push`
- any AWS-mutating command
- any static AWS credentials

## Outcome

The result of this patch is intentionally narrow:

- the first job now records the future auth-action invocation posture
- the job is still disabled
- workflow permissions remain unchanged
- later jobs are still disabled
- no deploy authority has been introduced

## Canonical Planning Artifact

The non-secret planning artifact for this patch is:

- [`.github/push-image-stage-oidc-auth-action-placeholder-patch.template.json`](./.github/push-image-stage-oidc-auth-action-placeholder-patch.template.json)

That file records the preserved lines, added auth-action placeholder messages,
and still-forbidden actions for this first job hunk.

## Source Boundary

Source may contain:

- patched comments
- patched placeholder step name
- patched placeholder `echo` lines
- preserved-line summary

Source must not contain:

- live action invocation
- credentials
- login/push commands
- workflow changes outside the first job hunk

## Governance Rules

- the auth-action placeholder patch must remain downstream of the invocation review
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

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_INVOCATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_INVOCATION_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-oidc-auth-action-placeholder-patch.template.json`](./.github/push-image-stage-oidc-auth-action-placeholder-patch.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_INVOCATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_INVOCATION_REVIEW_V1.md)
- [`.github/push-image-stage-ecr-login-command-invocation-review.template.json`](./.github/push-image-stage-ecr-login-command-invocation-review.template.json)

## Recommended Next Mission

The next bounded step after this patch should be:

- `Push Image Stage ECR Login Command Invocation Review v1`

That mission should remain review-only and define the exact future registry-login
command invocation posture after auth-action, permissions, login, and push
placeholders are all visible in source.

## Warning

Do not treat this patch as permission to invoke live auth actions.

It only records the future auth-action posture in the first disabled job while
preserving the non-deploying foundation posture.
