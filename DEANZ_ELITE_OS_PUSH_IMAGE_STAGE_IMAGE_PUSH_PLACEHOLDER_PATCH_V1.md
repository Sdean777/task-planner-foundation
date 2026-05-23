# Dean'z Elite OS Push Image Stage Image Push Placeholder Patch v1

## Purpose

This document records the first bounded image-push placeholder patch applied to
the `push-image-placeholder` job inside the `task-planner-foundation`
deployment workflow skeleton.

It exists to answer these questions after the image-push shape review:

- what exact first-job push-placeholder hunk was changed?
- what critical lines remained preserved?
- what future image-push posture is now visible in source?
- why does the workflow still remain disabled and non-deploying?

This document does not:

- enable `push-image-placeholder`
- add a live image-push step
- authenticate to AWS
- log in to ECR
- push an image
- create AWS trust
- change the Flask application contract

## Scope

This push-placeholder patch applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the already-reviewed future push hunk for the first disabled
job.

## Patch Objective

This patch exists to make the future first-job image-push posture explicit
while preserving zero deploy power.

The applied patch must remain:

- `push_placeholder_patch_applied`
- `push_placeholder_patch_still_disabled`
- `push_placeholder_patch_still_non_deploying`

## Applied Patch Footprint

The applied patch remains limited to the `push-image-placeholder` job.

The patch changed only:

- comments directly above `push-image-placeholder`
- one new placeholder step name inside that job
- placeholder `echo` lines describing the future image-push shape

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

## Added Push Placeholder Guidance

The patch adds only source-visible placeholder guidance for future missions:

- future image push must remain inside `push-image-placeholder`
- future image push must follow the future OIDC auth and ECR login steps
- future push posture must publish immutable `sha-<git-sha>` image truth first
- future `main` tag may exist only as a convenience mirror and must not replace the SHA tag
- no live push, ECS rollout, public verification, or static credentials are allowed in this mission

These additions are visible reminders only.

They do not introduce live registry mutation behavior.

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

- the first job now records the future image-push posture
- the job is still disabled
- workflow permissions remain unchanged
- later jobs are still disabled
- no deploy authority has been introduced

## Canonical Planning Artifact

The non-secret planning artifact for this patch is:

- [`.github/push-image-stage-image-push-placeholder-patch.template.json`](./.github/push-image-stage-image-push-placeholder-patch.template.json)

That file records the preserved lines, added push-placeholder messages, and
still-forbidden actions for this first job hunk.

## Source Boundary

Source may contain:

- patched comments
- patched placeholder step name
- patched placeholder `echo` lines
- preserved-line summary

Source must not contain:

- live push commands
- credentials
- rollout commands
- workflow changes outside the first job hunk

## Governance Rules

- the push-placeholder patch must remain downstream of the push-shape review
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

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-image-push-placeholder-patch.template.json`](./.github/push-image-stage-image-push-placeholder-patch.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_WIDENING_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_WIDENING_REVIEW_V1.md)
- [`.github/push-image-stage-push-job-permission-widening-review.template.json`](./.github/push-image-stage-push-job-permission-widening-review.template.json)

## Recommended Next Mission

The next bounded step after this patch should be:

- `Push Image Stage Push-Job Permission Widening Review v1`

That mission should remain review-only and define the exact future job-level
permission widening posture before any workflow-level or job-level permissions
change is introduced.

## Warning

Do not treat this patch as permission to add live image push.

It only records the future image-push posture in the first disabled job while
preserving the non-deploying foundation posture.
