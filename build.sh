#!/bin/bash
echo "Injecting build date..."
sed -i "s/__BUILD_DATE__/$(date -u +"%Y-%m-%dT%H:%M:%SZ")/" script.js