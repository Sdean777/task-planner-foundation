# Dean'z Elite OS Push Image Stage ECR Login Placeholder Patch v1

## Purpose

This document records the first bounded ECR-login placeholder patch applied to
the `push-image-placeholder` job inside the `task-planner-foundation`
deployment workflow skeleton.

It exists to answer these questions after the ECR-login shape review:

- what exact first-job login-placeholder hunk was changed?
- what critical lines remained preserved?
- what future ECR-login posture is now visible in source?
- why does the workflow still remain disabled and non-deploying?

This document does not:

- enable `push-image-placeholder`
- add a live ECR login step
- authenticate to AWS
- push an image
- create AWS trust
- change the Flask application contract

## Scope

This login-placeholder patch applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the already-reviewed future login hunk for the first disabled
job.

## Patch Objective

This patch exists to make the future first-job ECR-login posture explicit while
preserving zero deploy power.

The applied patch must remain:

- `login_placeholder_patch_applied`
- `login_placeholder_patch_still_disabled`
- `login_placeholder_patch_still_non_deploying`

## Applied Patch Footprint

The applied patch remains limited to the `push-image-placeholder` job.

The patch changed only:

- comments directly above `push-image-placeholder`
- one new placeholder step name inside that job
- placeholder `echo` lines describing the future ECR-login shape

The patch did not change:

- workflow-level permissions
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

## Added Login Placeholder Guidance

The patch adds only source-visible placeholder guidance for future missions:

- future ECR login placement must remain inside `push-image-placeholder`
- future login must follow the future OIDC auth step and precede any future image push
- future login shape must remain explicit `aws ecr get-login-password` to `docker login --password-stdin`
- future login inputs must remain explicit region and explicit registry URI from approved non-secret boundaries
- no live login, image push, ECS rollout, or static credentials are allowed in this mission

These additions are visible reminders only.

They do not introduce live registry behavior.

## Prohibited Content That Remains Absent

The applied patch still does not contain:

- `aws-actions/configure-aws-credentials`
- `aws ecr get-login-password`
- `docker login`
- `docker push`
- any AWS-mutating command
- any static AWS credentials

## Outcome

The result of this patch is intentionally narrow:

- the first job now records the future ECR-login posture
- the job is still disabled
- workflow permissions remain unchanged
- later jobs are still disabled
- no deploy authority has been introduced

## Canonical Planning Artifact

The non-secret planning artifact for this patch is:

- [`.github/push-image-stage-ecr-login-placeholder-patch.template.json`](./.github/push-image-stage-ecr-login-placeholder-patch.template.json)

That file records the preserved lines, added login-placeholder messages, and
still-forbidden actions for this first job hunk.

## Source Boundary

Source may contain:

- patched comments
- patched placeholder step name
- patched placeholder `echo` lines
- preserved-line summary

Source must not contain:

- live login commands
- credentials
- image-push commands
- workflow changes outside the first job hunk

## Governance Rules

- the login-placeholder patch must remain downstream of the login-shape review
- the patched job must remain disabled
- workflow permissions must remain unchanged in this mission
- later jobs must remain unchanged
- application code must remain untouched

## Explicit Non-Goals

This patch does not:

- enable any job
- create AWS trust
- create deployment automation
- authenticate to AWS
- log in to ECR
- push an image
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-ecr-login-placeholder-patch.template.json`](./.github/push-image-stage-ecr-login-placeholder-patch.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-image-push-shape-review.template.json`](./.github/push-image-stage-image-push-shape-review.template.json)

## Recommended Next Mission

The next bounded step after this patch should be:

- `Push Image Stage Image Push Shape Review v1`

That mission should remain review-only and define the exact future image-push
posture for the first job before any push command is introduced.

## Warning

Do not treat this patch as permission to add live ECR login.

It only records the future registry-login posture in the first disabled job
while preserving the non-deploying foundation posture.
