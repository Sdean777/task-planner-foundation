# Dean'z Elite OS Push Image Stage Placeholder-Bound Patch v1

## Purpose

This document records the first bounded workflow patch applied to the
`push-image-placeholder` job inside the `task-planner-foundation` deployment
workflow skeleton.

It exists to answer these questions after the controlled-patch review:

- what exact first-job hunk was changed?
- what critical lines remained preserved?
- what new placeholder guidance is now visible in source?
- why does the workflow still remain non-deploying?

This document does not:

- enable `push-image-placeholder`
- add AWS authentication
- log in to ECR
- push an image
- change the Flask application contract

## Scope

This placeholder-bound patch applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the first already-reviewed placeholder hunk.

## Patch Objective

This patch exists to make the first job more explicit while preserving zero
deploy power.

The applied patch must remain:

- `placeholder_patch_applied`
- `placeholder_patch_still_disabled`
- `placeholder_patch_still_non_deploying`

## Applied Patch Footprint

The applied patch remains limited to the `push-image-placeholder` job.

The patch changed only:

- comments directly above `push-image-placeholder`
- the step name inside that job
- placeholder `echo` lines inside that job

The patch did not change:

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
4. manual-only `workflow_dispatch`
5. `task-planner-foundation` service scope

## Added Placeholder Guidance

The patch adds only visible placeholder guidance for future missions:

- immutable image tags must remain `sha-<git-sha>`
- protected environment posture remains `production` on `refs/heads/main`
- future AWS trust posture remains GitHub OIDC only
- later jobs remain disabled
- no AWS authentication, ECR login, or image push is allowed in this mission

These additions are source-visible reminders only.

They do not introduce deploy behavior.

## Prohibited Content That Remains Absent

The applied patch still does not contain:

- `aws-actions/configure-aws-credentials`
- `aws ecr` commands
- `docker login`
- `docker push`
- any AWS-mutating command
- any secret-backed step

## Outcome

The result of this patch is intentionally narrow:

- the job is more explicit
- the job is still disabled
- the workflow is still manual-only
- later jobs are still disabled
- no deploy authority has been introduced

## Canonical Planning Artifact

The non-secret planning artifact for this patch is:

- [`.github/push-image-stage-placeholder-bound-patch.template.json`](./.github/push-image-stage-placeholder-bound-patch.template.json)

That file records the preserved lines, added placeholder messages, and still
forbidden actions for this first job hunk.

## Source Boundary

Source may contain:

- patched comments
- patched step name
- patched placeholder `echo` lines
- preserved-line summary

Source must not contain:

- live AWS commands
- credentials
- hidden enablement flags
- workflow changes outside the first job hunk

## Governance Rules

- the placeholder-bound patch must remain downstream of the controlled-patch review
- the patched job must remain disabled
- later jobs must remain unchanged
- application code must remain untouched

## Explicit Non-Goals

This patch does not:

- enable any job
- create AWS trust
- create deployment automation
- push an image
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [`.github/push-image-stage-placeholder-bound-patch.template.json`](./.github/push-image-stage-placeholder-bound-patch.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-github-oidc-auth-shape-review.template.json`](./.github/push-image-stage-github-oidc-auth-shape-review.template.json)

## Recommended Next Mission

The next bounded step after this patch should be:

- `Push Image Stage GitHub OIDC Auth Shape Review v1`

That mission should remain review-only and define the exact future auth posture
for this first job before any auth or registry commands are ever introduced.

## Warning

Do not treat this patch as workflow enablement.

It only makes the first disabled job more explicit while preserving the
non-deploying foundation posture.
