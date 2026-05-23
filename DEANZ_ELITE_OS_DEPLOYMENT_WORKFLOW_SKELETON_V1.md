# Dean'z Elite OS Deployment Workflow Skeleton v1

## Purpose

This document defines the first bounded deployment workflow skeleton for the
`task-planner-foundation` repository.

It exists to answer one narrow question:

> what should the first deployment workflow look like before any push or deploy
> stages are allowed to run?

This mission introduces only a skeleton. It does not introduce live deployment.

## Scope

This skeleton applies to:

- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md)
- [GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md](./GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It does not widen runtime authority, create AWS trust, or activate delivery.

## Skeleton Objective

The first workflow skeleton should:

- preserve the service scope to `task-planner-foundation`
- expose the intended stage order
- keep all deployment-bearing stages disabled
- make the gate and still-forbidden actions visible in source

## Allowed Skeleton Behavior

The first skeleton may:

- run on `workflow_dispatch`
- print readiness and gate reminders
- expose placeholder inputs such as environment or image tag
- show disabled ECR and ECS stages in source

The first skeleton must not:

- authenticate to AWS
- push to ECR
- register ECS task definitions
- update ECS services
- use deployment secrets

## Required Stage Shape

The first skeleton should preserve this stage order:

1. activation gate reminder
2. release/rollout context summary
3. disabled image-push stage
4. disabled ECS rollout stage
5. disabled public verification stage

This keeps the intended deployment path visible while preserving the current
non-deploying posture.

## Disablement Rules

The first skeleton must make disablement explicit:

- use comments explaining why push/deploy stages are off
- keep disabled jobs present but gated with `if: ${{ false }}`
- keep permissions narrow
- keep the workflow manual-only

That makes the repo honest: the shape exists, but the power does not.

## Source Boundary

Source may contain:

- placeholder workflow inputs
- disabled stage names
- gate reminders
- comments describing future behavior

Source must not contain:

- real AWS credentials
- live `aws` CLI deploy commands
- implicit enablement flags
- hidden deploy jobs

## Governance Rules

- the workflow skeleton must remain downstream of the activation gate
- the workflow skeleton must remain narrower than deployment execution
- the first enabled workflow must be a later, separate mission
- disabled stages must remain visible and intentional

## Explicit Non-Goals

This skeleton does not:

- perform ECR login
- perform ECR push
- perform ECS service update
- perform live smoke tests against a real environment
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md)
- [GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md](./GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)
- [DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md](./DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md)
- [`.github/protected-deployment-environment.template.json`](./.github/protected-deployment-environment.template.json)

## Follow-On Contract

This skeleton now pairs with the protected environment and approval boundary:

- [DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md](./DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md)
- [`.github/protected-deployment-environment.template.json`](./.github/protected-deployment-environment.template.json)

The next non-deploying AWS step after that should be:

- `Deployment Workflow Enablement Review Contract v1`

## Warning

Do not treat this skeleton as a deploy workflow.

It is a visible, disabled shape only.
