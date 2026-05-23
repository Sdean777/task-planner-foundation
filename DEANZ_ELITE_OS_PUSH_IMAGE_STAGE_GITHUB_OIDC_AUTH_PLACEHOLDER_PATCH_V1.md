# Dean'z Elite OS Push Image Stage GitHub OIDC Auth Placeholder Patch v1

## Purpose

This document records the first bounded auth-placeholder patch applied to the
`push-image-placeholder` job inside the `task-planner-foundation` deployment
workflow skeleton.

It exists to answer these questions after the auth-shape review:

- what exact first-job auth-placeholder hunk was changed?
- what critical lines remained preserved?
- what future GitHub OIDC auth posture is now visible in source?
- why does the workflow still remain disabled and non-deploying?

This document does not:

- enable `push-image-placeholder`
- add a live GitHub OIDC auth step
- create AWS trust
- log in to ECR
- push an image
- change the Flask application contract

## Scope

This auth-placeholder patch applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md)
- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the already-reviewed future auth hunk for the first disabled
job.

## Patch Objective

This patch exists to make the future first-job auth posture explicit while
preserving zero deploy power.

The applied patch must remain:

- `auth_placeholder_patch_applied`
- `auth_placeholder_patch_still_disabled`
- `auth_placeholder_patch_still_non_deploying`

## Applied Patch Footprint

The applied patch remains limited to the `push-image-placeholder` job.

The patch changed only:

- comments directly above `push-image-placeholder`
- one new placeholder step name inside that job
- placeholder `echo` lines describing the future OIDC auth shape

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

## Added Auth Placeholder Guidance

The patch adds only source-visible placeholder guidance for future missions:

- future job-local permission shape must remain `contents: read` plus `id-token: write`
- future auth placement must remain inside `push-image-placeholder`
- future trust references must remain repo-, branch-, environment-, and audience-bound
- future inputs must remain explicit AWS region and deterministic role session name only
- no static AWS credentials, live auth action, ECR login, or image push is allowed in this mission

These additions are visible reminders only.

They do not introduce live auth behavior.

## Prohibited Content That Remains Absent

The applied patch still does not contain:

- `aws-actions/configure-aws-credentials`
- `aws-access-key-id`
- `aws-secret-access-key`
- `aws ecr` commands
- `docker login`
- `docker push`
- any AWS-mutating command

## Outcome

The result of this patch is intentionally narrow:

- the first job now records the future OIDC auth posture
- the job is still disabled
- workflow permissions remain unchanged
- later jobs are still disabled
- no deploy authority has been introduced

## Canonical Planning Artifact

The non-secret planning artifact for this patch is:

- [`.github/push-image-stage-github-oidc-auth-placeholder-patch.template.json`](./.github/push-image-stage-github-oidc-auth-placeholder-patch.template.json)

That file records the preserved lines, added auth-placeholder messages, and
still-forbidden actions for this first job hunk.

## Source Boundary

Source may contain:

- patched comments
- patched placeholder step name
- patched placeholder `echo` lines
- preserved-line summary

Source must not contain:

- live auth steps
- credentials
- registry commands
- workflow changes outside the first job hunk

## Governance Rules

- the auth-placeholder patch must remain downstream of the auth-shape review
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
- push an image
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md)
- [`.github/push-image-stage-github-oidc-auth-placeholder-patch.template.json`](./.github/push-image-stage-github-oidc-auth-placeholder-patch.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-ecr-login-shape-review.template.json`](./.github/push-image-stage-ecr-login-shape-review.template.json)

## Recommended Next Mission

The next bounded step after this patch should be:

- `Push Image Stage ECR Login Shape Review v1`

That mission should remain review-only and define the exact future ECR login
posture for the first job before any registry command is introduced.

## Warning

Do not treat this patch as permission to add live GitHub OIDC auth.

It only records the future auth posture in the first disabled job while
preserving the non-deploying foundation posture.
