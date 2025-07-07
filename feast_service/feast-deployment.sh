#!/bin/bash

# Feast Local Deployment Script
# This script deploys a complete Feast service with all necessary components

set -e  # Exit on any error

FS_REPO_NAME="dsrp_fs_mle2"

uv run feast init $FS_REPO_NAME --template local

uv run feast ui --port 7001