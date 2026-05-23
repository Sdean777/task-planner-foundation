# Dean'z Elite OS Public Routing Baseline Standup v1

## Purpose

This document records the first explicit public-routing baseline standup for
the `task-planner-foundation` service after the initial bounded public
verification run was correctly blocked by missing stable routing.

It exists to answer these questions:

- what routing resources were created?
- what stable non-secret base URL now defines the public verification surface?
- what bounded compromises were used to expose the service safely?
- what remains out of scope even after the routing baseline exists?

This mission does not:

- change `app.py`
- change the first two workflow jobs
- claim that full release-gate verification is complete
- claim that the current routing surface is the final production form

## Scope

This routing standup applies to:

- [DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_VERIFICATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_VERIFICATION_RUN_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_PATCH_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_PATCH_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`aws/public-routing-baseline-standup.record.json`](./aws/public-routing-baseline-standup.record.json)

It governs only the explicit bounded public-routing baseline creation for the
service.

## Routing Baseline Objective

The objective of this mission was to replace the missing public verification
surface with a real bounded routing baseline:

- one explicit ALB listener
- one explicit target group
- one explicit ECS service-to-target-group attachment
- one explicit stable non-secret base URL
- one explicit `/health` reachability proof

That gives later public verification work an authoritative target instead of a
guessed task ENI address.

## Routing Resources Created

The following bounded routing resources were created or attached:

- ALB security-group ingress rule:
  `sgr-0d4e723fb59d2408a`
- ECS task security-group ingress rule:
  `sgr-015c272a44bf50856`
- target group:
  `arn:aws:elasticloadbalancing:us-east-1:329601960228:targetgroup/task-planner-foundation-tg/fded6d04a1294f24`
- listener:
  `arn:aws:elasticloadbalancing:us-east-1:329601960228:listener/app/deanzelite-alb/6c71a2d9ebd24918/b9754c82818e5a19`
- ECS service load-balancer attachment:
  `task-planner-foundation -> task-planner-foundation-tg -> containerPort 8081`

## Stable Base URL

The first stable non-secret `FOUNDATION_PUBLIC_BASE_URL` is now:

- `http://deanzelite-alb-2130825976.us-east-1.elb.amazonaws.com:8081`

This is the current bounded public-routing truth for the foundation service.

## Routing Design Choice

The routing baseline deliberately reuses the existing internet-facing
`deanzelite-alb`, but with a dedicated `HTTP :8081` listener for the
foundation service.

This was chosen because:

- the current HTTPS `443` listener already forwards all traffic to the existing
  `deanzelite-tg`
- the Flask foundation app exposes root-based endpoints only
- path-prefix routing without rewrite would have been wrong for `/health`,
  `/status`, `/validate`, and `/orchestrate`
- a dedicated listener isolates the foundation service without colliding with
  the current root listener behavior

This is a bounded routing baseline, not the final polished public edge.

## Security Boundary

The routing baseline required two explicit network adjustments:

- ALB SG `sg-07fce31d4ae9be1d4` now allows inbound `tcp/8081` from
  `0.0.0.0/0`
- ECS task SG `sg-0538f40fa41c92d64` now allows inbound `tcp/8081` from
  ALB SG `sg-07fce31d4ae9be1d4`

No broader security widening was introduced in this mission.

## Verified Outcome

The routing baseline is now real and usable:

- target group health is `healthy`
- ALB listener `:8081` exists and forwards to the foundation target group
- the ECS service is attached to the target group
- `GET /health` on the stable base URL returned:
  `{"status":"online"}`

Observed routing target:

- target IP:
  `172.31.12.8`
- target port:
  `8081`

At capture time, the ECS service had already returned to:

- desired count: `1`
- running count: `1`
- pending count: `0`
- primary rollout state: `COMPLETED`

## Bounded Routing Compromise

This routing baseline uses a shared existing ALB and a non-default listener
port instead of:

- a dedicated ALB
- a dedicated custom domain
- a host-header based 443 route

That compromise was accepted only because:

- it creates a stable non-secret base URL immediately
- it avoids colliding with the existing 443 default route
- it preserves the Flask root-path endpoint contract
- it keeps the mission bounded to routing standup, not full edge redesign

This is a bootstrap routing surface, not the final production-facing shape.

## Preserved Boundaries

This mission preserved the required boundaries:

- `app.py` stayed unchanged
- no AWS credentials were added to source
- no OpenAI keys were added
- `push-image-placeholder` behavior remained unchanged
- `ecs-rollout-placeholder` behavior remained unchanged
- no app-layer endpoint contract changed

## Canonical Execution Record

The non-secret execution record for this mission is:

- [`aws/public-routing-baseline-standup.record.json`](./aws/public-routing-baseline-standup.record.json)

That file records the created routing resources, stable base URL, and next
bounded mission.

## Recommended Next Mission

The next bounded step after this routing standup should be:

- `Telemetry Runtime Identity Alignment v1`

That mission should resolve the warning-bearing telemetry runtime drift now
revealed by the second bounded public verification run.

## Warning

Do not treat this routing baseline as the final public edge contract.

It creates a stable verification surface, but full public verification,
release-gate judgment, and later edge hardening remain separate bounded
stages.
