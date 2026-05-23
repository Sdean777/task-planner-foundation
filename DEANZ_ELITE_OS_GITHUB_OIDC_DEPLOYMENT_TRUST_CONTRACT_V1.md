# Dean'z Elite OS GitHub OIDC Deployment Trust Contract v1

## Purpose

This document defines the first bounded GitHub OIDC deployment trust contract
for the `task-planner-foundation` AWS path.

It exists to answer these questions before any live deployment automation is
attempted:

- which GitHub repository may request deployment trust later?
- which branch or environment boundaries are acceptable?
- which audience and claim shapes should be expected?
- what must remain explicitly deferred until live deployment work begins?

This document does not:

- create an OIDC provider
- create an IAM role
- create a trust policy
- add a deployment workflow
- deploy anything

## Scope

This contract applies only to the future deployment posture for:

- [GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md](./GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)

It does not widen the current foundation runtime.

## Trust Subject

The only future repository eligible for this trust path is:

- GitHub owner: `Sdean777`
- GitHub repository: `task-planner-foundation`

No broader organization-wide or wildcard repository trust should be assumed.

## Trust Audience

The future AWS audience should be:

- `sts.amazonaws.com`

That keeps the trust path aligned with standard AWS role assumption through
GitHub OIDC.

## Branch And Environment Boundary

The first acceptable trust posture should be narrow:

- primary ref: `refs/heads/main`
- optional later manual environment boundary: `production`

Current rule:

- no wildcard branch trust
- no blanket trust for all tags
- no trust for forks
- no trust for arbitrary repositories in the owner account

## Workflow Boundary

Future trust should be limited to an explicit deployment workflow, not every
GitHub Actions job in the repo.

Current posture:

- deployment workflow is not created yet
- trust must stay deferred until that workflow exists

Future bounded direction:

- one explicit deploy workflow file
- one explicit deployment role assumption point
- one explicit image-push and ECS-update path

## Claim Expectations

The future trust posture should be derived from GitHub OIDC claims that are
specific enough to avoid broad trust.

Expected claim dimensions:

- repository owner/name
- branch ref
- workflow identity or reusable-workflow origin
- audience
- optional protected environment

The trust shape should not accept a generic “any job in any repo” model.

## Deferred Trust Rules

The following remain explicitly deferred in this mission:

- concrete provider ARN
- final role ARN
- final trust policy JSON
- final environment protection rules
- final workflow filename for deployment

Those decisions belong in the first live deployment-automation planning phase,
not here.

## Source Boundary

Source may contain:

- repository name
- owner name
- intended audience
- allowed branch/environment posture
- placeholder role names and provider placeholders

Source must not contain:

- live AWS credentials
- real trust policies copied from production
- deployable IAM role documents with account-specific identifiers

## Current Minimum-Trust Posture

The minimum acceptable posture for future deployment trust is:

- one repository
- one primary branch
- one future deployment role
- one AWS audience
- no wildcard subjects
- no long-lived AWS keys in GitHub secrets

## Canonical Planning Artifact

The non-secret planning artifact for this trust boundary is:

- [aws/github-oidc-deployment-trust.template.json](./aws/github-oidc-deployment-trust.template.json)

That file is a planning artifact only.

It is not an IAM trust policy and must not be pasted directly into production
without review.

## Drift And Block Rules

Future live deployment work should be blocked if any of these conditions occur:

- wildcard repository trust is proposed
- wildcard branch trust is proposed
- trust allows forks or unrelated repos
- long-lived AWS keys are used as a shortcut instead of OIDC
- deployment trust is documented separately from the identity boundary

## Governance Rules

- trust boundaries must remain narrower than runtime role boundaries
- deployment trust must remain separate from task runtime identity
- repository/branch/environment restrictions must be documented before use
- live trust creation must wait for a dedicated deployment workflow mission

## Explicit Non-Goals

This contract does not:

- create an AWS IAM OIDC provider
- create a deploy role
- create a deploy workflow
- add ECR push logic
- add ECS update automation
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md)
- [GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md](./GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md)
- [aws/github-oidc-deployment-trust.template.json](./aws/github-oidc-deployment-trust.template.json)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [aws/ecr-image-promotion-ecs-rollout.template.json](./aws/ecr-image-promotion-ecs-rollout.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-github-oidc-auth-shape-review.template.json`](./.github/push-image-stage-github-oidc-auth-shape-review.template.json)

## Downstream Push-Image Auth Review

The deployment-trust boundary is now paired with a narrower first-job review
layer:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-github-oidc-auth-shape-review.template.json`](./.github/push-image-stage-github-oidc-auth-shape-review.template.json)

That downstream layer exists to keep the exact future auth-step shape explicit
before any auth step is introduced into the workflow source.

## Follow-On Contract

This trust boundary now pairs with the rollout handoff boundary:

- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [aws/ecr-image-promotion-ecs-rollout.template.json](./aws/ecr-image-promotion-ecs-rollout.template.json)

The next non-deploying AWS step after that should be:

- `Public Runtime Verification & Release Gate Contract v1`

## Warning

Do not start live AWS deployment from this contract alone.

This is still a bounded planning artifact for a foundation service.
