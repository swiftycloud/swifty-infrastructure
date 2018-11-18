#!/usr/bin/env bash

docker build --network=host -t registry.gitlab.com/swiftyteam/swifty-infrastructure/gitlab-runner .
docker push registry.gitlab.com/swiftyteam/swifty-infrastructure/gitlab-runner:latest