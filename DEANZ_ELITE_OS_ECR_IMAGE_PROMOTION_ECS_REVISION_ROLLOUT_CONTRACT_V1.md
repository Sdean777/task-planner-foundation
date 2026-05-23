# Dean'z Elite OS ECR Image Promotion & ECS Revision Rollout Contract v1

## Purpose

This document defines the first bounded contract for moving a verified
container artifact into a future ECS task-definition revision and service
rollout.

It exists to answer these questions before any live deployment automation is
attempted:

- which image tags are trusted for rollout?
- which tags are convenience-only and must not drive deployment truth?
- how should a new ECS task-definition revision be created?
- how must rollback stay possible?

This document does not:

- push images to ECR
- update an ECS service
- add deployment automation
- create AWS credentials
- change the Flask application contract

## Scope

This contract applies to the current foundation deployment-planning chain:

- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md)
- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [aws/ecs-task-definition.template.json](./aws/ecs-task-definition.template.json)

It does not widen the current non-deploying foundation runtime.

## Promotion Truth Rules

The future rollout path must treat image identity and rollout identity
separately:

- image truth = immutable image URI with SHA-based tag
- rollout truth = explicit ECS task-definition revision referencing that image

Neither mutable tags nor human memory should be treated as deployment truth.

## Tag Classes

### 1. Immutable Deployment Tag

Required deployment tag shape:

- `sha-<git-sha>`

This is the only approved source-of-truth tag for rollout decisions.

### 2. Convenience Tag

Allowed convenience tag:

- `main`

This may exist for operator visibility, but it must not be the only rollout
input.

### 3. Disallowed Rollout Tags

The following must not drive deployment truth:

- `latest`
- ad hoc manual tags with no traceability
- unversioned environment tags with no SHA linkage

## Promotion Stages

The first bounded promotion ladder should remain simple:

1. local verification artifact
   - output of `container-build-verify.yml`
   - not deployable by itself
2. candidate image
   - built artifact tagged with `sha-<git-sha>`
3. convenience mirror tag
   - optional `main`
4. rollout target
   - explicit ECS task-definition revision referencing the immutable SHA image

At no stage should a mutable tag replace the SHA-based deployment truth.

## ECS Revision Handoff Rules

Each future rollout must produce a new task-definition revision that:

- preserves the task family name
- preserves the container name
- changes the image reference intentionally
- keeps non-secret environment values stable unless separately reviewed

The service update should point to:

- one explicit task-definition revision
- one explicit image URI

It must not depend on an in-place retag of a mutable image as a hidden rollout
mechanism.

## Service Update Posture

When future live rollout work exists, the first service update posture should
remain narrow:

- one service
- one desired count baseline
- one task family
- one explicit revision jump at a time
- no parallel widening of app configuration

This keeps rollout traceability simple for the foundation service.

## Rollback Rules

Rollback must remain revision-based, not guess-based.

Minimum rollback posture:

- keep the previous task-definition revision identifiable
- keep the previous SHA-tagged image identifiable
- rollback to the previous known-good revision, not to a mutable tag
- fail closed if the previous good revision cannot be identified

## Drift And Block Rules

Future live rollout work should be blocked if any of these conditions occur:

- rollout relies on `latest`
- task-definition revision is updated without explicit image SHA linkage
- app configuration changes are bundled silently into the same rollout without review
- previous revision is not recorded for rollback
- service update posture is broader than the current foundation service scope

## Source Boundary

Source may contain:

- tag-shape rules
- task-family naming intent
- rollout sequence rules
- rollback posture rules
- placeholder image URIs and revision metadata

Source must not contain:

- production image digests copied from a real account
- live deployment scripts in this mission
- real AWS credentials

## Canonical Planning Artifact

The non-secret rollout planning artifact is:

- [aws/ecr-image-promotion-ecs-rollout.template.json](./aws/ecr-image-promotion-ecs-rollout.template.json)

That file is a planning artifact only.

It is not a deploy script and not a live release manifest.

## Governance Rules

- immutable image identity must exist before rollout identity
- rollout identity must be explicit at the task-definition revision layer
- rollback identity must remain available before service update is attempted
- image promotion and ECS revision updates must stay separate from application code changes

## Explicit Non-Goals

This contract does not:

- create an ECR repository
- push images to ECR
- register task definitions
- update an ECS service
- add GitHub deploy jobs
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md)
- [aws/ecr-image-promotion-ecs-rollout.template.json](./aws/ecr-image-promotion-ecs-rollout.template.json)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [aws/public-runtime-verification-release-gate.template.json](./aws/public-runtime-verification-release-gate.template.json)
- [DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-ecr-login-shape-review.template.json`](./.github/push-image-stage-ecr-login-shape-review.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-image-push-shape-review.template.json`](./.github/push-image-stage-image-push-shape-review.template.json)

## Downstream Push-Image Login Review

The rollout boundary is now paired with a narrower first-job review layer:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-ecr-login-shape-review.template.json`](./.github/push-image-stage-ecr-login-shape-review.template.json)

That downstream layer exists to keep the exact future registry-login posture
explicit before any login step is introduced into the workflow source.

## Downstream Push-Image Push Review

The rollout boundary is also paired with the next narrower first-job review
layer:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-image-push-shape-review.template.json`](./.github/push-image-stage-image-push-shape-review.template.json)

That downstream layer exists to keep the exact future image-publication posture
explicit before any push step is introduced into the workflow source.

## Downstream Rollout Candidate Review

This rollout boundary now pairs with the bounded second-job review layer:

- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CANDIDATE_REVIEW_V1.md)
- [`.github/ecs-rollout-stage-candidate-review.template.json`](./.github/ecs-rollout-stage-candidate-review.template.json)

That downstream layer exists to keep the still-disabled
`ecs-rollout-placeholder` job reviewable without introducing live
task-definition registration or ECS service updates.

## Downstream Rollout Enablement Proposal

This rollout boundary now also pairs with the narrower second-job proposal
layer:

- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [`.github/ecs-rollout-stage-enablement-proposal.template.json`](./.github/ecs-rollout-stage-enablement-proposal.template.json)

That downstream layer exists to keep the exact future rollout-job diff shape
explicit before any controlled patch review is allowed.

## Downstream Rollout Controlled Patch Review

This rollout boundary now also pairs with the narrower second-job controlled
patch-review layer:

- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [`.github/ecs-rollout-stage-controlled-patch-review.template.json`](./.github/ecs-rollout-stage-controlled-patch-review.template.json)

That downstream layer exists to keep the exact rollout-job review boundary
explicit before any second-job patch is allowed.

## Downstream Rollout Patch

This rollout boundary now also pairs with the bounded second-job patch layer:

- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_PATCH_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_PATCH_V1.md)
- [`.github/ecs-rollout-stage-patch.template.json`](./.github/ecs-rollout-stage-patch.template.json)

That downstream layer exists to keep the exact rollout-job live patch explicit
before any actual rollout run is attempted.

## Recommended Next Mission

The next bounded step after this contract and the first bounded image
publication run should be:

- `First Bounded ECS Rollout Run v1`

## Warning

Do not start live AWS deployment from this contract alone.

This is still a bounded planning artifact for a foundation service.
