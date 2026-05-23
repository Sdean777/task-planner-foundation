# GitHub Actions AWS Foundation Placeholder Plan

This is the planning document for the future AWS deployment workflow for
`task-planner-foundation`.

Parts of this plan are now bounded and executable, but later-stage expansion
still remains intentionally staged.

Current active workflow artifacts include:

- `.github/workflows/container-build-verify.yml`
- `.github/workflows/deploy-foundation-skeleton.yml`
- `.github/workflows/public-runtime-smoke.yml`

The container bridge remains non-deploying and requires no secrets.

The deployment skeleton now contains bounded manual jobs for image publication,
ECS rollout, and public verification, but the broader chain still remains
governed by the contracts recorded below.

The next planning artifact is the explicit ECS runtime contract:

- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [aws/ecs-task-definition.template.json](./aws/ecs-task-definition.template.json)

The next operator-facing planning layer is the ECS service runbook:

- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)

The next service-parameter boundary is the environment contract:

- [DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md)
- [aws/ecs-service-parameters.template.json](./aws/ecs-service-parameters.template.json)

The next service IAM boundary is the identity and access contract:

- [DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md)
- [aws/ecs-identity-access-boundary.template.json](./aws/ecs-identity-access-boundary.template.json)

The next GitHub trust boundary is the OIDC deployment trust contract:

- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [aws/github-oidc-deployment-trust.template.json](./aws/github-oidc-deployment-trust.template.json)

The next rollout boundary is the immutable image and ECS revision contract:

- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [aws/ecr-image-promotion-ecs-rollout.template.json](./aws/ecr-image-promotion-ecs-rollout.template.json)

The next release boundary is the public runtime verification gate:

- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [aws/public-runtime-verification-release-gate.template.json](./aws/public-runtime-verification-release-gate.template.json)

The next third-job review boundary after ECS baseline standup is the public
verification candidate review:

- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md)
- [`.github/public-verification-stage-candidate-review.template.json`](./.github/public-verification-stage-candidate-review.template.json)

The next third-job proposal boundary is the public verification enablement
proposal:

- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [`.github/public-verification-stage-enablement-proposal.template.json`](./.github/public-verification-stage-enablement-proposal.template.json)

The next third-job controlled patch review boundary is the public verification
controlled patch review:

- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [`.github/public-verification-stage-controlled-patch-review.template.json`](./.github/public-verification-stage-controlled-patch-review.template.json)

The next third-job patch boundary is the public verification patch:

- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_PATCH_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_PATCH_V1.md)
- [`.github/public-verification-stage-patch.template.json`](./.github/public-verification-stage-patch.template.json)

The next workflow-introduction boundary is the deployment activation gate:

- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md)
- [aws/deployment-workflow-activation-gate.template.json](./aws/deployment-workflow-activation-gate.template.json)

The next workflow artifact is the disabled deployment skeleton:

- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

The next approval boundary is the protected deployment environment contract:

- [DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md](./DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md)
- [`.github/protected-deployment-environment.template.json`](./.github/protected-deployment-environment.template.json)

The next enablement boundary is the workflow enablement review contract:

- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md)
- [`.github/deployment-workflow-enablement-review.template.json`](./.github/deployment-workflow-enablement-review.template.json)

The next single-job review boundary is the push-image candidate review:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md)
- [`.github/push-image-stage-candidate-review.template.json`](./.github/push-image-stage-candidate-review.template.json)

The next single-job proposal boundary is the push-image enablement proposal:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [`.github/push-image-stage-enablement-proposal.template.json`](./.github/push-image-stage-enablement-proposal.template.json)

The next single-job patch-review boundary is the controlled patch review:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [`.github/push-image-stage-controlled-patch-review.template.json`](./.github/push-image-stage-controlled-patch-review.template.json)

The next first-job workflow patch record is the placeholder-bound patch:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md)
- [`.github/push-image-stage-placeholder-bound-patch.template.json`](./.github/push-image-stage-placeholder-bound-patch.template.json)

The next first-job auth-shape review boundary is the GitHub OIDC auth review:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-github-oidc-auth-shape-review.template.json`](./.github/push-image-stage-github-oidc-auth-shape-review.template.json)

The next first-job auth-placeholder patch record is the OIDC auth patch:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-github-oidc-auth-placeholder-patch.template.json`](./.github/push-image-stage-github-oidc-auth-placeholder-patch.template.json)

The next first-job registry-login review boundary is the ECR-login shape review:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-ecr-login-shape-review.template.json`](./.github/push-image-stage-ecr-login-shape-review.template.json)

The next first-job registry-login placeholder patch record is the ECR-login patch:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-ecr-login-placeholder-patch.template.json`](./.github/push-image-stage-ecr-login-placeholder-patch.template.json)

The next first-job image-publication review boundary is the image-push shape review:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md)
- [`.github/push-image-stage-image-push-shape-review.template.json`](./.github/push-image-stage-image-push-shape-review.template.json)

The next first-job image-publication placeholder patch record is the push patch:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-image-push-placeholder-patch.template.json`](./.github/push-image-stage-image-push-placeholder-patch.template.json)

The next first-job permission review boundary is the push-job permission review:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_WIDENING_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_WIDENING_REVIEW_V1.md)
- [`.github/push-image-stage-push-job-permission-widening-review.template.json`](./.github/push-image-stage-push-job-permission-widening-review.template.json)

The next first-job permission placeholder patch record is the permission patch:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-push-job-permission-placeholder-patch.template.json`](./.github/push-image-stage-push-job-permission-placeholder-patch.template.json)

The next first-job auth-action review boundary is the OIDC auth-action review:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_INVOCATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_INVOCATION_REVIEW_V1.md)
- [`.github/push-image-stage-oidc-auth-action-invocation-review.template.json`](./.github/push-image-stage-oidc-auth-action-invocation-review.template.json)

The next first-job auth-action placeholder patch record is the auth-action patch:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-oidc-auth-action-placeholder-patch.template.json`](./.github/push-image-stage-oidc-auth-action-placeholder-patch.template.json)

The next first-job registry-login command review boundary is the login-command review:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_INVOCATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_INVOCATION_REVIEW_V1.md)
- [`.github/push-image-stage-ecr-login-command-invocation-review.template.json`](./.github/push-image-stage-ecr-login-command-invocation-review.template.json)

The first first-job registry-login command placeholder patch record is the
login-command patch:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-ecr-login-command-placeholder-patch.template.json`](./.github/push-image-stage-ecr-login-command-placeholder-patch.template.json)

The refreshed first-job live-enable candidate review boundary is the
live-enable review:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md)
- [`.github/push-image-stage-live-enable-candidate-review.template.json`](./.github/push-image-stage-live-enable-candidate-review.template.json)

The refreshed first-job live-enable proposal boundary is the live-enable
proposal:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md)
- [`.github/push-image-stage-live-enable-proposal.template.json`](./.github/push-image-stage-live-enable-proposal.template.json)

The refreshed first-job live-enable controlled patch review boundary is the
live-enable controlled patch review:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CONTROLLED_PATCH_REVIEW_V1.md)
- [`.github/push-image-stage-live-enable-controlled-patch-review.template.json`](./.github/push-image-stage-live-enable-controlled-patch-review.template.json)

The refreshed first-job live-enable patch boundary is the live-enable patch:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PATCH_V1.md)
- [`.github/push-image-stage-live-enable-patch.template.json`](./.github/push-image-stage-live-enable-patch.template.json)

## Purpose

Document the intended workflow shape without:

- adding AWS credentials
- adding live deployment secrets
- enabling automatic production deployment
- widening the scope of this foundation repo

## Intended Workflow Shape

```text
on:
  push to main
  pull request to main
  optional manual dispatch

jobs:
  1. lint-and-validate
  2. container-build-verify
  3. push-image-to-ecr
  4. deploy-to-ecs-fargate
  5. public-runtime smoke test
```

## Planned Stages

### 1. Lint and Validate

- check out source
- set up Python
- install requirements
- run existing CI checks
- run endpoint-level validation if lightweight tests are added later

### 2. Container Build Verification

Current active bridge step.

- build from `docker/Dockerfile`
- tag locally as `task-planner-foundation:test`
- run the container locally in CI
- smoke test `/health`, `/validate`, and `/orchestrate`
- remove the test container after verification
- do not push the image anywhere
- do not require AWS credentials or deployment secrets

### 3. Push Image to ECR

- authenticate to AWS with GitHub OIDC or scoped credentials
- push image to Amazon ECR
- record image URI as a deployment artifact

### 4. Deploy to ECS/Fargate

- update ECS task definition image reference
- deploy to ECS service
- keep environment variables externalized
- keep the service stateless

### 5. Public Runtime Smoke Test

- test `/health`
- test `/validate`
- test `/orchestrate`
- fail the rollout if the foundation contract is broken

## Required Future Inputs

These are not added now, but will be required later:

- AWS account and region selection
- ECR repository name
- ECS cluster and service names
- IAM/OIDC trust configuration
- deployment environment boundaries
- rollout and rollback policy

## Security Rules

- do not commit static AWS credentials
- prefer GitHub OIDC over long-lived secrets
- keep environment configuration out of source when it becomes sensitive
- keep deployment permissions scoped to this service

## Portability Rules

- keep the app runnable locally without GitHub Actions
- keep the container runnable outside AWS
- avoid workflow logic that assumes ECS is the only future runtime forever

## Current Status

The existing live workflows remain:

- `.github/workflows/ci.yaml`
- `.github/workflows/validate-with-registry.yaml`
- `.github/workflows/container-build-verify.yml`
- `.github/workflows/deploy-foundation-skeleton.yml` with a bounded first-job push-image path only

Current completed/active step:

- non-deploying container build verification
- ECS runtime contract planning
- ECS service runbook planning
- ECS parameterization and environment contract planning
- ECS identity and access boundary planning
- GitHub OIDC deployment trust planning
- ECR image promotion and ECS rollout planning
- Public runtime verification and release-gate planning
- Deployment workflow activation-gate planning
- Deployment workflow skeleton planning
- Protected deployment environment and approval planning
- Deployment workflow enablement-review planning
- Push-image stage candidate-review planning
- Push-image stage enablement-proposal planning
- Push-image stage controlled-patch-review planning
- Push-image stage placeholder-bound patch
- Push-image stage GitHub OIDC auth-shape review
- Push-image stage GitHub OIDC auth-placeholder patch
- Push-image stage ECR-login shape review
- Push-image stage ECR-login placeholder patch
- Push-image stage image-push shape review
- Push-image stage image-push placeholder patch
- Push-image stage push-job permission-widening review
- Push-image stage push-job permission placeholder patch
- Push-image stage OIDC auth-action invocation review
- Push-image stage OIDC auth-action placeholder patch
- Push-image stage ECR-login command invocation review
- Push-image stage ECR-login command placeholder patch
- Push-image stage live-enable candidate review
- Push-image stage live-enable proposal
- Push-image stage live-enable controlled patch review
- Push-image stage live-enable patch
- first bounded ECR image publication run
- ECS rollout stage candidate review
- ECS rollout stage enablement proposal
- ECS rollout stage controlled patch review
- ECS rollout stage patch
- first bounded ECS rollout run attempt (blocked at missing service baseline)
- ECS service baseline standup
- public verification stage candidate review
- public verification stage enablement proposal
- public verification stage controlled patch review
- public verification stage patch
- first bounded public verification run attempt (blocked at missing stable public base URL)
- public routing baseline standup
- second bounded public verification run (`manual_review_required` due telemetry runtime drift)
- telemetry runtime identity alignment (`keep_active` restored after bounded ECS revision 2 rollout)
- post-deploy public runtime smoke tests (`keep_active` held across three ALB-backed smoke rounds)
- public runtime smoke automation review (`candidate_ready` for a later read-only automation proposal)
- public runtime smoke automation proposal (`proposal_ready_for_controlled_patch_review` with one future read-only workflow file only)
- public runtime smoke automation controlled patch review (`ready_for_patch` with one future read-only workflow file and no deploy-workflow mutation)
- public runtime smoke automation patch (`public-runtime-smoke.yml` created as a separate read-only workflow)
- first bounded public runtime smoke automation run (`stable` through local-equivalent workflow-path execution against the ALB base URL)
- GitHub-hosted public runtime smoke workflow dispatch review (`candidate_ready` for a later repository-backed hosted-dispatch proposal)
- GitHub-hosted public runtime smoke workflow dispatch proposal (`ready_for_controlled_run_review` without workflow mutation or hosted execution)
- GitHub-hosted public runtime smoke workflow dispatch controlled run review (`ready_for_first_bounded_run` without workflow mutation or hosted execution)
- first bounded GitHub-hosted public runtime smoke workflow dispatch run (`blocked` because the smoke workflow chain is still local untracked source state, not tracked repository source`)
- GitHub-hosted public runtime smoke workflow source publication (`publishes the bounded smoke workflow chain into tracked and pushed repository source`)
- second bounded GitHub-hosted public runtime smoke workflow dispatch run (`blocked` because FOUNDATION_PUBLIC_BASE_URL is missing in GitHub repository variables`)
- GitHub-hosted public runtime smoke workflow variable baseline (`FOUNDATION_PUBLIC_BASE_URL` created as the explicit non-secret repository variable for the published smoke workflow)
- third bounded GitHub-hosted public runtime smoke workflow dispatch run (`success` against the published workflow and repository-variable baseline)
- GitHub-hosted public runtime smoke success source publication (`publishes the blocked retry, variable baseline, successful hosted run, and updated doctrine chain as tracked repository source`)
- CloudWatch service telemetry baseline review (`logs-only baseline confirmed; explicit service telemetry connection still not yet present`)
- CloudWatch service telemetry baseline proposal (`minimum explicit service-telemetry shape defined over the existing awslogs -> CloudWatch path`)
- CloudWatch service telemetry controlled patch review (`exact future app.py diff locked to one helper, one import, and one /telemetry emission call`)
- CloudWatch service telemetry patch (`reviewed app.py diff implemented, immutable sha-a72c3be9ac74a70e841735e1cc6feebf9af08c62 rolled to task-planner-foundation:3, /telemetry response unchanged, and structured service_telemetry_snapshot confirmed in CloudWatch`)
- CloudWatch service telemetry source publication (`publishes the local telemetry runtime commit, patch doctrine, patch evidence, and updated chain as tracked repository source`)
- CloudWatch service telemetry metric-filter baseline review (`structured snapshot present, metric filters absent, alarms absent, and proposal stage now justified`)
- CloudWatch service telemetry metric-filter proposal (`first metric filter scoped to DeanzElite/Foundation with explicit anti-collision boundary against Atlas and sovereign OS telemetry names`)
- CloudWatch service telemetry metric-filter controlled patch review (`exact one-filter CloudWatch mutation locked to the foundation log group, namespace, and metric name with Atlas name reuse blocked`)
- CloudWatch service telemetry metric-filter patch (`one reviewed metric filter created on /deanz-elite/task-planner-foundation, metric visible in DeanzElite/Foundation, and Atlas name reuse still blocked`)
- CloudWatch service telemetry metric-filter source publication (`publishes the local metric-filter review, proposal, controlled review, patch doctrine, patch evidence, and updated chain as tracked repository source`)

Still future:

- CloudWatch Service Telemetry Alarm Baseline Review v1

This plan now includes bounded first-job image publication and bounded
second-job rollout paths plus a real ECS service baseline and a completed
third-job candidate review, proposal, controlled review, patch, blocked first
public-verification execution attempt, stable routing baseline, and second
verification run. Telemetry runtime identity alignment and repeatable
post-deploy smoke proof are now complete, the smoke-automation review
boundary, proposal shape, controlled patch boundary, first read-only smoke
workflow patch, first bounded automation run, hosted-dispatch review,
hosted-dispatch proposal, hosted-dispatch controlled run review, the first
bounded hosted-dispatch run, source publication, and repository-variable
baseline are now recorded. The second bounded hosted-dispatch retry is also
recorded as blocked at missing repository-variable input, and the third
bounded hosted-dispatch run is now recorded as successful. The hosted-smoke
success source-publication checkpoint now closes that local source gap, and the
CloudWatch service telemetry baseline review now confirms the current
CloudWatch layer is logs-only, and the baseline proposal now defines the
minimum explicit service-telemetry shape. The controlled patch review now
locks the exact future `app.py` diff. The telemetry patch now completes that
reviewed `app.py` change, keeps the public contract stable, and proves the
structured snapshot is present in CloudWatch. The source-publication
checkpoint now converges the local runtime commit and CloudWatch telemetry
evidence into tracked repository source. The metric-filter baseline review now
confirms that the structured snapshot is present while the metric and alarm
layers remain absent. The metric-filter proposal now defines the minimum
foundation-scoped metric namespace and blocks Atlas or sovereign telemetry name
reuse. The controlled patch review now locks the exact one-filter CloudWatch
mutation boundary. The metric-filter patch now creates that one reviewed filter
and proves the metric is visible in `DeanzElite/Foundation` without widening
into alarms or Atlas convergence. The source-publication checkpoint now
converges the local metric-filter doctrine and patch evidence into tracked
repository source. The next bounded stage is CloudWatch service telemetry
alarm baseline review.
